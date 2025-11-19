# 🌇 The Dusk Boundary Line

_A narrative-driven indie game that explores burnout, emotional boundaries, and the fragile balance of adult life._

---

## 🎮 About

**The Dusk Boundary Line** follows **Arya**, a 28-year-old data analyst trapped in the endless cycle of overwork and family debt. Through atmospheric storytelling and emotionally reactive gameplay, players experience the weight of **modern burnout**, the **struggle to set boundaries**, and the **search for meaning amid exhaustion**.

Set in a liminal world between day and night, the game symbolically mirrors the blurred boundaries between **work and personal life**, **rest and productivity**, and **dreams and despair**.

---

## 🌌 Theme

> “Sometimes, survival feels like choosing which part of yourself to sacrifice.”

The central theme revolves around **professional burnout**, **boundaries**, and **the cost of endurance**.  
Every choice Arya makes carries emotional consequences—each decision pushing him closer to either healing or collapse.

---

## 💡 Core Experience

- Navigate through shifting environments that reflect Arya’s emotional states  
- Experience the **gradual descent into burnout** and the difficult path toward recovery  
- Discover **moments of clarity** hidden between work and exhaustion  
- Find meaning in the **grey zone** between productivity and peace  
- Shape Arya’s destiny through **branching narrative routes**

---

## 🚀 Getting Started

### Prerequisites

- [Twine](https://twinery.org/)
- [Renpy](https://www.renpy.org/)
- [Git](https://git-scm.com/)
- [VSCODE](https://code.visualstudio.com/)

## 🎯 Features

- [ ] [Feature 1]
- [ ] [Feature 2]
- [ ] [Feature 3]

### Project Structure

```
├── Assets/         # Game assets (sprites, audio, models)
├── Scripts/        # Game logic and code
├── Scenes/         # Game scenes/levels
└── Docs/           # Documentation
```

## 📝 Roadmap

- [ ] Initial game mechanics implementation
- [ ] Level design and world building
- [ ] Character system development
- [ ] UI/UX polish
- [ ] Audio integration
- [ ] Beta testing
- [ ] Release preparation

## 👥 Authors

- **Hafizh Ahmad Al-Abror** - *Programmer* - 707082330117 - [xyukii](https://github.com/xyukii)
- **Isaac Hope Marcelino Purba** - *Assets* - 707082300122 - [isaacpurba1](https://github.com/isaacpurba1)
- **Muhammad Andhika Widyadhana** - *Story Designer* - 707082300151 - [gatrix23](https://github.com/gatrix23)
- **Achmad zaky** - *Story Progression* - 707082330112 - [Fryndazs](https://github.com/Fryndazs/)

## 🙏 Acknowledgments

- [Credit contributors, asset creators, inspirations]
- [Special thanks]

## 📞 Contact

Project Link: [https://github.com/xyukii/thedusk-boundaryline-game](https://github.com/xyukii/thedusk-boundaryline-game)

---

⭐ Star this repository if you find it interesting!


**GUI Customization**

- **Files changed/added:**: `Main/game/screens.rpy` (main menu now uses image buttons) and `Main/game/screens_custom.rpy` (new helper screens `start_or_load` and `settings_menu`).
- **Button images:**: The main menu uses the images in `gui/button/`:
	- `play@2.png` — main "Mulai" image button
	- `settings@2.png` — settings hub image button
	- `quit@2.png` — quit image button

- **Behavior summary:**: The `Mulai` button opens `start_or_load`, which offers "Mulai Baru" (Start New) and "Muat" (Load). The `Settings` button opens a hub that links to `preferences`, `about`, and `help`. The `Quit` button calls `Quit(confirm=True)` and will show Ren'Py's confirmation.

- **How to change button images or add hover states:**
	- Replace the files in `gui/button/` with your own art keeping the same filenames.
	- If you want hover variants, add files with a consistent naming scheme and update `screens.rpy` to point `hover` to them (e.g. `play_hover.png`).

- **Customizing labels or layout:**
	- Edit `Main/game/screens.rpy` to adjust `xalign`, `yalign`, `spacing`, or wrap the menu in additional `frame`/`vbox` containers.
	- `Main/game/screens_custom.rpy` contains the small helper screens; you can edit these to merge content into a single screen, convert links to transcluded content, or change button styles.

- **Keeping in-game menus unchanged:**: No in-game menu screens (`game_menu`, `navigation`, quick menu, etc.) were altered; only the main menu layout was changed. All save/load/preferences functionality remains intact.

- **Testing locally:**
	- Open the Ren'Py launcher and run the project (select the folder `Main` in the launcher). From the main menu you should see the three image buttons. Click them to verify behavior.

- **Revert or experiment safely:**
	- If you want to keep the original main menu while experimenting, rename the file `Main/game/screens.rpy` to a backup (`screens.rpy.bak`) and copy the original back when needed, or version-control the branch.

- **Next steps (optional):**
	- Add hover/pressed image variants for more polish.
	- Replace the settings hub links with transcluded content (tabs) if you prefer a single-screen settings experience.
	- Add theme variables to `Main/game/gui.rpy` for tunable colors/sizes for easier customization by non-programmers.

