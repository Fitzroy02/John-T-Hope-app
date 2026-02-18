# Device Safety Profiles - Examples

This directory contains example device safety profiles demonstrating how the `device_safety_profile.schema.json` is applied in practice.

## Purpose

Device safety profiles document the governance requirements for healthcare devices referenced in educational content. These examples show how different device types (from low-risk thermometers to high-risk specialist devices) are governed.

## Schema Reference

All profiles follow the schema defined in `/schemas/device_safety_profile.schema.json`

## Example Profiles to Create

When implementing device content, example profiles might include:

### Low-Risk, General Awareness
- Thermometer
- Bandages
- Ice pack
- Hand sanitizer

### Moderate-Risk, General Use
- Blood pressure monitor
- Heating pad
- First aid kit items
- Pulse oximeter

### High-Risk, Specialist Devices
- EpiPen (epinephrine auto-injector)
- Insulin pump
- Inhaler (prescription asthma medication)
- Blood glucose monitor (for diabetics)
- Nebulizer

## How to Use

1. Before creating content about a healthcare device, create or reference its safety profile
2. Use the profile to determine:
   - Appropriate age restrictions
   - Content approach (awareness vs. usage information)
   - Parental consent requirements
   - Review and approval requirements
3. Technical systems use profiles to enforce access controls

## Profile Creation Process

See `DEVICE_SAFETY_GOVERNANCE.md` for the full device safety framework and profile creation process.

---

**Note**: Actual device profiles should be created as part of content development. This directory serves as the designated location for those profiles.
