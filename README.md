# POS Cashdrawer Action Menu

**Version:** 19.0.1.0.0  
**Author:** Cositt Technology  
**License:** LGPL-3  
**Category:** Sales/Point of Sale

## Overview

This module enhances the Odoo Point of Sale interface by moving the cash drawer opening action to the main action menu. It provides quick and easy access to the cash drawer control functionality, improving operational efficiency in retail and restaurant environments.

The module leverages Odoo's native hardware proxy capabilities, ensuring compatibility with all supported POS cash drawer hardware configurations including Epson ePOS and IoT devices.

## Features

- **Integrated Cash Drawer Control:** Quick-access button to open the cash drawer from the main POS action menu
- **Hardware Compatibility:** Works seamlessly with any supported POS cash drawer hardware (Epson ePOS, IoT Box, etc.)
- **Clean UI:** Removes redundant cash drawer button from the payment screen to declutter the interface
- **Conditional Display:** Cash drawer button only appears when hardware is properly configured
- **Odoo 19 Compatible:** Fully integrated with Odoo 19 Enterprise Point of Sale

## Installation

1. Place the module folder in your Odoo addons directory:
   ```bash
   cp -r cs_pos_cashdrawer_menu /path/to/odoo/addons/
   ```

2. Update the module list in Odoo:
   - Navigate to **Apps** > **Update Apps List**
   - Search for "POS Cashdrawer Action Menu"

3. Install the module:
   - Click **Install** on the module card

## Configuration

### Prerequisites

- Point of Sale module must be installed
- A cash drawer device must be connected and configured in your POS hardware setup

### Setting Up Hardware

1. Go to **Point of Sale > Configuration > Point of Sale**
2. Select the POS terminal configuration
3. Under the **Hardware** section, enable:
   - **Enable Cash Drawer** (`iface_cashdrawer`)
   - Configure the appropriate hardware interface (Epson ePOS, IoT, etc.)
4. Save the configuration

## Usage

### Opening the Cash Drawer

1. **From the Main Action Menu:**
   - In the main POS interface, locate the action menu (typically in the top bar)
   - Click the **"Abrir caja"** (Open Cash Drawer) button
   - The cash drawer will open immediately

2. **Visual Indicator:**
   - The cash drawer button displays a **archive icon** (📦) for easy identification
   - The button only appears when cash drawer hardware is enabled in the POS configuration

### Payment Screen

- The redundant cash drawer button has been removed from the payment screen
- All cash drawer operations go through the main action menu for a cleaner interface

## Technical Details

### Dependencies

- `point_of_sale` (Odoo core module)

### Template Inheritance

The module uses Odoo's XML template inheritance system to:

1. **Add cash drawer button to ControlButtons:**
   - Inherits from `point_of_sale.ControlButtons`
   - Inserts a new button before the price list button
   - Conditionally displays based on `pos.config.iface_cashdrawer`

2. **Remove cash drawer button from PaymentScreenButtons:**
   - Inherits from `point_of_sale.PaymentScreenButtons`
   - Hides the native cash drawer button to avoid duplication

### Key Components

- **Template:** `cashdrawer_menu.xml`
  - `ControlButtons` override: Main action menu customization
  - `PaymentScreenButtons` override: Removes redundant UI element

## Troubleshooting

### Cash Drawer Button Not Appearing

**Problem:** The cash drawer button is not visible in the action menu.

**Solution:**
1. Verify that `Enable Cash Drawer` is checked in the POS configuration
2. Confirm that the hardware proxy is properly configured
3. Restart the POS terminal application
4. Clear browser cache (Ctrl+Shift+Delete)

### Cash Drawer Not Opening

**Problem:** Clicking the button does not open the cash drawer.

**Solution:**
1. Check that the cash drawer device is properly connected
2. Verify hardware configuration in POS settings
3. Test the hardware connection independently
4. Check Odoo server logs for hardware proxy errors
5. Ensure IoT Box (if used) is online and connected

### Button Appearing Twice

**Problem:** Cash drawer button appears in both action menu and payment screen.

**Solution:**
1. Ensure module is properly installed (check **Installed Modules**)
2. Restart the POS terminal
3. Perform a browser cache clear and page refresh

## Support

For issues, feature requests, or technical support:
- **Website:** https://cositt.com
- **Email:** support@cositt.com

## License

This module is licensed under LGPL-3. See LICENSE file for details.

## Changelog

### Version 19.0.1.0.0
- Initial release for Odoo 19 Enterprise
- Added cash drawer button to main action menu
- Integrated with native hardware proxy
- Removed redundant payment screen button
