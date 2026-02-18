# Country Profiles - Examples

This directory contains example country profiles demonstrating how the `country_profile.schema.json` is applied in practice.

## Purpose

Country profiles document legal and cultural factors affecting healthcare content delivery in specific jurisdictions. These examples show how content governance adapts across different legal frameworks, cultural contexts, and healthcare systems.

## Schema Reference

All profiles follow the schema defined in `/schemas/country_profile.schema.json`

## Example Profiles to Create

When implementing healthcare content for specific countries, example profiles might include:

### Tier 1 Countries (Full Implementation)
Countries with large user bases requiring comprehensive profiles:
- United States (US)
- United Kingdom (GB)
- Canada (CA)
- Australia (AU)

### Tier 2 Countries (Secondary Markets)
Countries with significant user bases:
- India (IN)
- Japan (JP)
- Germany (DE)
- France (FR)

### Tier 3 Countries (General Availability)
Countries with basic profiles for general compliance:
- Other markets as needed

## Profile Components

Each country profile should document:

1. **Legal Framework**
   - Age of medical consent
   - Restricted topics
   - Mandatory reporting requirements
   - Data protection laws
   - Parental consent/notification laws

2. **Cultural Context**
   - Communication style preferences
   - Individualism vs. collectivism
   - Family involvement expectations
   - Stigmatized health topics
   - Traditional medicine integration
   - Gender and religious considerations

3. **Healthcare System**
   - System overview (universal, private, mixed)
   - Access considerations
   - Provider types

4. **Emergency Resources**
   - Emergency services number
   - Crisis hotlines
   - Text and online support services

## How to Use

1. When entering a new market, create a country profile
2. Use the profile to:
   - Configure age restrictions
   - Implement consent requirements
   - Adapt content culturally
   - Provide appropriate resources
   - Ensure legal compliance
3. Technical systems use profiles to enforce jurisdiction-specific rules

## Profile Creation Process

See `COUNTRY_PROFILES_LEGAL_VARIATION.md` for the full framework and profile creation process.

---

**Note**: Actual country profiles should be created as part of market expansion. This directory serves as the designated location for those profiles.
