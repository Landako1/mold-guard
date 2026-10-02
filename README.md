# 🛡️ Mold Guard for Home Assistant

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Landako1&repository=mold-guard&category=integration)

**Mold Guard** is a custom integration for Home Assistant designed to prevent mold growth—especially in cooler homes (18–20 °C)—by calculating **absolute humidity** ($g/m^3$) and alerting household members when mold-critical thresholds are reached.

---

## ✨ Features

- **Absolute Humidity Calculation:** Automatically calculates absolute humidity ($g/m^3$) using the Magnus formula from temperature and relative humidity sensors. No manual YAML template sensors required!
- **Targeted Mold Protection Thresholds:** Pre-configured with a conservative threshold of **8.5 g/m³** (approx. 55% relative humidity at 18 °C) to protect cold outer walls.
- **Smart Outdoor Comparison:** Ensures indoor air is at least **1.5 g/m³** more humid than outdoor air before recommending ventilation.
- **UI Config Flow:** Easily add rooms and assign sensors directly via the Home Assistant UI.

---

## 🚀 Quick Installation

Click the button above or follow these manual steps:

1. Open **HACS** in your Home Assistant instance.
2. Click on the **three dots** in the top right corner and select **Custom repositories**.
3. Paste the URL of this repository:
   `https://github.com/Landako1/mold-guard`
4. Select **Integration** as the Category and click **Add**.
5. Click **Explore & Download Repositories**, search for **Mold Guard**, and install it.
6. Restart Home Assistant.

---

## ⚙️ Configuration

1. Go to **Settings → Devices & Services → Add Integration**.
2. Search for **Mold Guard**.
3. Fill in your room details:
   - **Room Name:** (e.g., *Bedroom*)
   - **Temperature & Humidity Sensors:** Select indoor sensors.
   - **Outdoor Sensors:** Select outdoor weather station sensors.
   - **Notification Service:** (e.g., `notify.alle_handys`)
4. Save and enjoy automated mold prevention!

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
