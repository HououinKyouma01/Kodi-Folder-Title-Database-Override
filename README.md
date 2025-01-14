# Kodi Folder Title Database Override Plugin

🎬 **Restore Original Series Titles from Folder Names!**  
This plugin ensures your media library displays the **original titles** from your folder structure, overriding scraped or translated titles from metadata providers. Perfect for anime fans and anyone who prefers original titles over localized ones!


## Important: Backup Your Database ⚠️

Before using this plugin, it is **strongly recommended** to back up your Kodi database. While the plugin is designed to work safely, unexpected issues can occur due to different configurations or folder structures.

### How to Backup Your Database

1. **Locate Your Database Folder**:
   - **Windows**: `C:\Users\<YourUsername>\AppData\Roaming\Kodi\userdata\Database\`
   - **Linux**: `~/.kodi/userdata/Database/`
   - **macOS**: `~/Library/Application Support/Kodi/userdata/Database/`

2. **Backup the Files**:
   - Copy the Database folder to safe location

3. **Restore if Needed**:
   - If something goes wrong, replace the `Database` folder with your backup.

### Why Backup?
- The plugin modifies your Kodi database directly.
- If your folder structure is unconventional, titles might be updated incorrectly.
- A backup ensures you can restore your library to its previous state.

---

## Why This Plugin? 🎯

Many media scrapers (like TheTVDB or TMDB) provide **translated titles** instead of the original ones. For example:
- Your folder: `G:\Anime\Shigatsu wa Kimi no Uso`
- Scraped title: `Your Lie in April`

This plugin fixes this by:
1. Using your **folder names** as the source of truth for series titles.
2. Overriding scraped or translated titles with the **original names** from your folder structure.
3. Ensuring consistency across your library.

---

## Features ✨

- **Original Title Restoration**: Use folder names to override scraped or translated titles.
- **Flexible Folder Support**: Works with any folder structure (e.g., `C:\Anime\SeriesName\Season 1\S01E01.mkv`).
- **Special Folder Handling**: Skips `extras`, `specials`, and other non-series folders.
- **Force Update Option**: Override all titles at once with a single click.
- **Logging**: Detailed logs to track changes and troubleshoot issues.

---

## Installation 📥

### Step 1: Download the Plugin
1. Download the latest release from the [Releases page](https://github.com/yourusername/folder-title-override/releases).
2. Extract the `.zip` file.

### Step 2: Install in Kodi
1. Copy the extracted folder to your Kodi addons directory:
   - **Windows**: `C:\Users\<YourUsername>\AppData\Roaming\Kodi\addons\`
   - **Linux**: `~/.kodi/addons/`
   - **macOS**: `~/Library/Application Support/Kodi/addons/`
2. Restart Kodi.

### Step 3: Enable the Plugin
1. Go to **Add-ons** → **My Add-ons** → **Program Add-ons**.
2. Enable the **Folder Title Override** plugin.

---

## Usage 🚀

### Step 1: Configure the Plugin
1. Open the plugin from the Kodi add-ons menu.
2. Set your **Base Directories** (e.g., `G:\Anime` or `C:\Media\TV Shows`).
3. Configure the following options:
   - **Force Update**: Override all titles, even if they already match the folder name.
   - **Log Level**: Set to `Debug` for detailed logs or `Info` for basic logs.

### Step 2: Run the Plugin
1. Click **Run** to start the title override process.
2. Watch as your library gets updated with the original folder-based titles!

---

## Supported Folder Structures 🌟

| Folder Structure                                      | Resulting Title                     |
|-------------------------------------------------------|-------------------------------------|
| `G:\Anime\Shigatsu wa Kimi no Uso\Season 1\S01E01.mkv`| `Shigatsu wa Kimi no Uso`           |
| `C:\Media\TV Shows\Anime\Kimi no Na wa\S01E01.mkv`    | `Kimi no Na wa`                     |
| `D:\Anime\SeriesName\extras\featurette.mkv`           | Skipped (special folder)            |
| `E:\Anime\SeriesName (2023)\Season 1\S01E01.mkv`      | `SeriesName (2023)`                 |

---

## Options Explained ⚙️

### 1. **Base Directories**
- Set the root folders where your media is stored (e.g., `G:\Anime`).
- The plugin will scan these folders for series to update.

### 2. **Force Update**
- When enabled, the plugin will override **all titles**, even if they already match the folder name.
- Use this to fix titles that were previously updated incorrectly.

### 3. **Log Level**
- **Info**: Basic logs showing which titles were updated.
- **Debug**: Detailed logs for troubleshooting (e.g., folder paths, skipped files).

---

## Examples 🖼️

### Before:
- Folder: `G:\Anime\Shigatsu wa Kimi no Uso`
- Scraped Title: `Your Lie in April`

### After Running the Plugin:
- Folder: `G:\Anime\Shigatsu wa Kimi no Uso`
- Updated Title: `Shigatsu wa Kimi no Uso`

---

## Troubleshooting 🛠️

### 1. Titles Not Updating
- Ensure the plugin has access to your media folders.
- Check the logs for errors or skipped files.

### 2. Incorrect Titles
- Verify your folder structure matches the expected format:
  ```
  Base Directory
  └── SeriesName
      ├── Season 1
      │   └── S01E01.mkv
      └── extras
          └── featurette.mkv
  ```
  or
  
  - Verify your folder structure matches the expected format:
  ```
  Base Directory
  └── SeriesName
      ├── S01E01.mkv
  ```

### 3. Logs Not Showing
- Set the log level to `Debug` in the plugin settings.

---

## Contributing 🤝

Contributions are welcome! Feel free to:
- Open an issue for bugs or feature requests.
- Submit a pull request with improvements.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️
✨ Happy organizing! ✨
