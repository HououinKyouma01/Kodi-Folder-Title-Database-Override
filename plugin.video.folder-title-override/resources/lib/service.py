import os
import xbmc
import xbmcvfs
import xbmcaddon
import sqlite3
import logging
from logging.handlers import RotatingFileHandler

class TitleOverride:
    def __init__(self):
        self.addon = xbmcaddon.Addon()
        self.video_db_path = xbmcvfs.translatePath('special://database/MyVideos*.db')
        
        # Add configuration option
        self.force_all = self.addon.getSetting('force_all') == 'true'
        
        # Set up logging in user's profile directory
        log_path = xbmcvfs.translatePath('special://profile/addon_data/plugin.video.folder-title-override/')
        if not xbmcvfs.exists(log_path):
            xbmcvfs.mkdirs(log_path)
        
        self.log_file = os.path.join(log_path, 'folder_title_override.log')
        
        self.logger = logging.getLogger('FolderTitleOverride')
        self.logger.setLevel(logging.INFO)
        
        # Create rotating file handler
        handler = RotatingFileHandler(
            self.log_file,
            maxBytes=1024*1024,  # 1MB
            backupCount=3
        )
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        self.logger.addHandler(handler)
        self.logger.info("Folder Title Override service initialized")

    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)

    def get_latest_db(self):
        # Get database directory
        db_dir = xbmcvfs.translatePath('special://database/')
        self.log(f"Looking for video database in: {db_dir}")
        
        # List all MyVideos databases
        try:
            db_files = [f for f in os.listdir(db_dir) if f.startswith('MyVideos') and f.endswith('.db')]
            self.log(f"Found database files: {db_files}")
            
            if not db_files:
                self.log("No video databases found", logging.ERROR)
                return None
                
            # Find the latest version
            latest_db = max(db_files, key=lambda x: int(x[9:-3]))  # Extract version number from filename
            db_path = os.path.join(db_dir, latest_db)
            self.log(f"Using database: {db_path}")
            return db_path
            
        except Exception as e:
            self.log(f"Error finding database: {str(e)}", logging.ERROR)
            return None

    def update_titles(self, immediate_refresh=False):
        self.log("Starting title updates for TV shows")
        if self.force_all:
            self.log("Force all updates enabled via configuration")
        
        db_path = self.get_latest_db()
        if not db_path:
            self.log("Could not find video database", logging.ERROR)
            xbmc.executebuiltin('Notification("Folder Title Override", "Could not find video database", 5000)')
            return

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        try:
            # Get all TV shows with their paths
            cursor.execute("""
                SELECT tvshow.idShow, tvshow.c00, path.strPath 
                FROM tvshow
                JOIN episode ON tvshow.idShow = episode.idShow
                JOIN files ON episode.idFile = files.idFile
                JOIN path ON files.idPath = path.idPath
                GROUP BY tvshow.idShow
            """)
            series = cursor.fetchall()

            if not series:
                self.log("No TV shows found in database", logging.WARNING)
                xbmc.executebuiltin('Notification("Folder Title Override", "No TV shows found in database", 5000)')
                return

            update_count = 0
            for show_id, current_title, path in series:
                norm_path = os.path.normpath(path)
                
                # Get the actual series folder name
                path_parts = norm_path.split(os.sep)
                
                # Skip the drive letter (first part)
                if len(path_parts) > 0 and ':' in path_parts[0]:
                    path_parts = path_parts[1:]
                
                # Find the series folder by looking for the first non-base directory
                series_folder = None
                for i, part in enumerate(path_parts):
                    if part.lower() not in ['anime', 'tv shows', 'series']:
                        # Check if this is a season folder
                        if part.lower().startswith('season'):
                            # Get the parent folder
                            if i > 0:
                                series_folder = path_parts[i-1]
                        else:
                            series_folder = part
                        break
                
                if not series_folder:
                    self.log(f"Skipping base directory: {norm_path}")
                    continue
                
                # Skip special folders
                if series_folder.lower() in ['extrafanart', 'extrathumbs', 'extras', 'specials']:
                    self.log(f"Skipping special subfolder: {norm_path}")
                    continue
                
                # Always update when force_all is True
                if self.force_all:
                    cursor.execute("UPDATE tvshow SET c00=? WHERE idShow=?", (series_folder, show_id))
                    update_count += 1
                    self.log(f"Force updated series {show_id}: {current_title} -> {series_folder}")
                    continue
                
                # Normal update when folder name doesn't match
                if series_folder and series_folder != current_title:
                    cursor.execute("UPDATE tvshow SET c00=? WHERE idShow=?", (series_folder, show_id))
                    update_count += 1
                    self.log(f"Updated series {show_id}: {current_title} -> {series_folder}")

            conn.commit()
            
            if update_count > 0:
                self.log(f"Updated {update_count} TV show titles")
                xbmc.executebuiltin(f'Notification("Folder Title Override", "Updated {update_count} TV show titles", 5000)')
                if immediate_refresh:
                    xbmc.executebuiltin('UpdateLibrary(video)')
            else:
                self.log("No TV show titles needed updating")
                xbmc.executebuiltin('Notification("Folder Title Override", "No TV show titles needed updating", 5000)')

        except sqlite3.Error as e:
            self.log(f"Database error: {str(e)}", logging.ERROR)
            xbmc.executebuiltin('Notification("Folder Title Override", "Database error occurred", 5000)')
        finally:
            conn.close()

if __name__ == '__main__':
    monitor = xbmc.Monitor()
    override = TitleOverride()

    # Use the configuration setting instead of force_update parameter
    override.update_titles()
    override.log("Service completed") 