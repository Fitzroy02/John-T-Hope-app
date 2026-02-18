# Device Safety Governance

**Healthcare Device and Tool Safety Framework**

---

## Purpose

This document establishes governance principles and assessment processes for healthcare-related devices, tools, and equipment referenced in educational content.

---

## Scope

This framework applies to:
- Medical devices referenced in educational content
- Health monitoring tools
- First aid equipment
- Personal protective equipment in healthcare contexts
- Any physical device or tool related to health or medical care

This framework does NOT apply to:
- Digital health apps (separate governance)
- General wellness products (unless making medical claims)
- Food or nutrition products (unless medical nutrition)

---

## Device Safety Principles

### 1. Age-Appropriate Device Information

**Principle**: Device information must match developmental capacity and legal authority.

**Application**:
- Young children: Awareness-only (e.g., "thermometers measure temperature")
- Adolescents: Usage understanding for appropriate devices (e.g., blood pressure monitors)
- Age restrictions clearly stated for specialist devices
- Parental involvement required for device usage by minors

---

### 2. Risk-Proportionate Governance

**Principle**: Governance oversight scales with device risk level.

**Application**:
- Low-risk devices (thermometers, band-aids): Standard content review
- Moderate-risk devices (blood glucose monitors, nebulizers): Enhanced review + medical consultation
- High-risk devices (EpiPens, defibrillators): Maximum governance + legal review + medical expert approval

---

### 3. Clear Safety Boundaries

**Principle**: Device safety information must be clear without substituting for professional instruction.

**Application**:
- Content explains WHAT a device is and WHY it exists
- Content does NOT provide step-by-step usage instructions for high-risk devices
- Content emphasizes professional training for specialist devices
- Content directs to manufacturer instructions and healthcare provider guidance

---

### 4. Regulatory Awareness

**Principle**: Content acknowledges regulatory status and variation.

**Application**:
- Regulatory approval status mentioned where relevant (e.g., "approved by FDA," "CE marked")
- Variation across jurisdictions acknowledged
- Unapproved or experimental devices clearly identified
- No promotion of devices lacking regulatory approval

---

### 5. No Commercial Endorsement

**Principle**: Content remains device-neutral, not brand-specific.

**Application**:
- Generic device categories discussed (e.g., "blood pressure monitors"), not specific brands
- Exceptions only when device type has single dominant brand (e.g., "EpiPen" as recognizable term), but generic term also provided
- No commercial partnerships influencing content
- No affiliate links or commercial incentives

---

### 6. Cultural and Economic Accessibility

**Principle**: Device content acknowledges accessibility variation.

**Application**:
- Awareness that not all devices available in all contexts
- Cost considerations acknowledged
- Alternative approaches presented where devices unavailable
- No assumption of universal device access

---

## Device Categories

Devices are categorized by risk level, informing governance requirements.

### Category 1: Awareness-Only Devices

**Definition**: Devices that children and adolescents may encounter but should not use independently.

**Examples**:
- Thermometers (for older children/teens with supervision)
- Stethoscopes
- Blood pressure cuffs
- Pulse oximeters

**Content Approach**:
- Explain what device does
- Explain why healthcare providers use it
- Age-appropriate detail about how it works
- No independent usage instructions
- Emphasize professional use

**Governance**: Standard content review

---

### Category 2: General-Use Devices

**Definition**: Devices that appropriately trained individuals (including older adolescents with supervision) may use under appropriate circumstances.

**Examples**:
- First aid supplies (bandages, antiseptic wipes)
- Thermometers (for self-monitoring by older teens)
- Heating pads
- Blood glucose monitors (for diabetic teens with training)

**Content Approach**:
- Explain device purpose
- General safety considerations
- When to seek professional help
- Acknowledge training required for medical devices
- Direct to manufacturer instructions

**Governance**: Standard review + age-appropriateness assessment

---

### Category 3: Specialist Devices

**Definition**: Devices requiring specific medical training or prescription.

**Examples**:
- Inhalers (require prescription and training)
- EpiPens (require prescription and training)
- Insulin pumps (require prescription and extensive training)
- Continuous glucose monitors
- Nebulizers

**Content Approach**:
- Explain device purpose and importance
- Emphasize prescription requirement
- Emphasize professional training requirement
- Explain why proper training matters
- NO step-by-step usage instructions
- Direct to healthcare provider and manufacturer

**Governance**: Enhanced review + medical expert consultation + age restrictions

---

## Device Safety Profile Schema

Each device referenced in content has a safety profile. See `/schemas/device_safety_profile.schema.json` for technical schema.

### Required Fields

**Device Name**: Generic device name (not brand)

**Category**: 
- awareness_only
- general_use
- specialist_device

**Risk Level**:
- low (minimal harm if misused)
- moderate (potential for harm if misused)
- high (serious harm possible if misused)

**Age Tier Restrictions**: 
Array of minimum ages for different content levels:
- awareness_age: Minimum age for awareness content
- supervised_use_age: Minimum age for supervised usage information
- independent_use_age: Minimum age for independent usage information (if applicable)

**Requires Parental Consent**: Boolean
- true if parental consent required for content access
- false if age verification alone sufficient

**Notes**: Additional context (regulatory status, cultural variation, etc.)

---

## Content Development Process

### Step 1: Device Identification
Content creator identifies device to be referenced.

### Step 2: Safety Profile Creation
Device safety profile created using schema.

### Step 3: Category Assignment
Device assigned to appropriate category.

### Step 4: Content Development
Content developed according to category requirements.

### Step 5: Review
Content reviewed by:
- Standard reviewer (all devices)
- Medical expert (specialist devices)
- Legal reviewer (high-risk devices)

### Step 6: Approval and Publication
Content approved and published with appropriate access controls.

---

## Enforcement

### Prohibited Content
The following is explicitly prohibited:

❌ Step-by-step usage instructions for specialist devices  
❌ Encouragement of device usage without professional guidance  
❌ Dismissal of professional training requirements  
❌ Brand-specific promotion or endorsement  
❌ Unapproved or experimental devices presented as safe/proven  
❌ Device usage by age groups below safety profile restrictions  

### Escalation
Content violating device safety principles:
1. Flagged immediately
2. Removed from production
3. Reviewed by governance lead
4. Addressed before republication

---

## Country-Specific Variation

Device availability, regulatory status, and usage norms vary by country. See `COUNTRY_PROFILES_LEGAL_VARIATION.md` for country-specific handling.

**General Principle**: Content acknowledges variation and adapts where necessary for major markets.

---

## Review Cycle

This framework is reviewed:
- Annually
- When new device categories are introduced
- Upon significant regulatory changes
- At the request of medical advisory board (if established)

---

## Related Documents

- `device_safety_profile.schema.json` - Technical schema for device profiles
- `/examples/device_safety_profiles/` - Example device profiles
- `HEALTHCARE_GOVERNANCE_PRINCIPLES.md` - Foundational principles
- `HEALTHCARE_CONTENT_CATEGORIES.md` - Content categorization framework

---

**Last Updated**: 2026-02-18  
**Next Review**: 2027-02-18  
**Document Owner**: Governance Lead  
**Version**: 1.0
