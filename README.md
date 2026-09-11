# MTG Custom Cards for TCG Arena

This is a ready-to-use custom instance of the official TCG-Arena MTG mod,  
configured so **you can easily add your own custom cards**.

## Files included

| File | Purpose |
|------|---------|
| `Game_MTG_Custom.json` | The main game definition (board, formats, rules...) |
| `cards.json` | Your card database (starts with basic lands + 5 example custom cards) |
| `add_custom_card.py` | Simple script to add new cards easily |

## How to make it live (5 minutes)

### 1. Create a GitHub repository
1. Go to https://github.com/new
2. Name it e.g. `mtg-custom`
3. Make it **Public**
4. Click "Create repository"

### 2. Upload the files
1. Click "uploading an existing file"
2. Upload:
   - `Game_MTG_Custom.json`
   - `cards.json`
3. Commit the changes

### 3. Enable GitHub Pages
1. Go to the repo → **Settings** → **Pages**
2. Under "Source" choose **Deploy from a branch**
3. Branch: `main` / folder: `/ (root)`
4. Save
5. Wait 1-2 minutes

Your files will be available at:
```
https://YOUR_USERNAME.github.io/mtg-custom/cards.json
https://YOUR_USERNAME.github.io/mtg-custom/Game_MTG_Custom.json
```

### 4. Edit the game file
1. Open `Game_MTG_Custom.json` on GitHub → Edit
2. Replace this line:
   ```json
   "dataUrl": "https://YOUR_GITHUB_USERNAME.github.io/mtg-custom/cards.json",
   ```
   with your real username, e.g.:
   ```json
   "dataUrl": "https://johnsmith.github.io/mtg-custom/cards.json",
   ```
3. Commit the change

### 5. Generate the play link
1. Go to https://tcg-arena.fr/build
2. Paste the URL of your game file:
   ```
   https://YOUR_USERNAME.github.io/mtg-custom/Game_MTG_Custom.json
   ```
3. Copy the generated link
4. Open it → your custom MTG game appears!

## Adding your own custom cards

### Option A – Easy (use the Python script)
```bash
python add_custom_card.py
```
It will ask you for name, cost, colors, image URL, etc. and update `cards.json`.

Then re-upload the new `cards.json` to GitHub.

### Option B – Manual
Edit `cards.json` and add a new entry like this:

```json
"my-super-card": {
  "id": "my-super-card",
  "name": "My Super Card",
  "type": "Creature",
  "cost": 3,
  "Colors": ["R", "G"],
  "Card type": "Creature — Dragon",
  "Color identity": ["R", "G"],
  "isHorizontal": false,
  "face": {
    "front": {
      "name": { "name": "My Super Card" },
      "type": "Creature",
      "cost": 3,
      "isHorizontal": false,
      "image": "https://i.imgur.com/your-image.jpg"
    }
  },
  "power": 4,
  "toughness": 4,
  "_legal": {
    "EDH": true,
    "MD": true,
    "VI": true,
    "ST": true,
    "PA": true,
    "LG": true,
    "PI": true
  }
}
```

**Important**: The image must be a **direct public URL** (Imgur, ImgChest, GitHub raw, etc.).

After updating `cards.json`, just re-upload it.  
You can also bump the `"version"` number in `Game_MTG_Custom.json` so players re-download the cards.

## Hosting card images
Recommended free options:
- https://imgur.com (upload → right click → copy image address)
- https://imgchest.com
- GitHub itself (put images in an `/images` folder in the same repo)

## Notes
- The current `cards.json` has only 10 cards so the game loads instantly.
- All original MTG formats (EDH, Modern, Standard, etc.) and board layout are kept.
- You can later merge the official huge Scryfall database if you want both official + custom cards.

Enjoy your custom MTG on TCG Arena!
