# Country Profiles & Legal Variation

**Adapting Healthcare Content Across Jurisdictions**

---

## Purpose

This document establishes the framework for adapting healthcare content to respect legal, cultural, and regulatory variation across countries and jurisdictions.

---

## Core Principle

Healthcare content must adapt to:
- **Legal requirements** (age of consent, restricted topics, mandatory reporting)
- **Cultural contexts** (health beliefs, stigma, communication norms)
- **Healthcare system variation** (access to care, insurance models, provider types)
- **Regulatory frameworks** (device approval, medication availability, treatment standards)

One-size-fits-all healthcare content is inappropriate and potentially harmful.

---

## Country Profile System

Each supported country has a profile documenting legal and cultural factors affecting healthcare content.

See `/schemas/country_profile.schema.json` for technical schema.

### Profile Components

**Country Name**: Official country name

**Age of Medical Consent**: 
Age at which individuals can consent to healthcare without parental involvement (varies significantly)

**Restricted Topics**: 
Array of topics legally restricted or culturally sensitive:
- Topics illegal to discuss with minors
- Topics requiring special handling
- Topics culturally taboo or highly sensitive

**Cultural Considerations**:
Key cultural factors affecting healthcare content:
- Communication norms (direct vs. indirect)
- Family involvement expectations
- Stigmatized conditions
- Traditional medicine integration
- Gender-specific considerations
- Religious healthcare considerations

**Legal Notes**:
Additional legal requirements:
- Mandatory reporting obligations
- Data protection requirements specific to health data
- Parental notification laws
- Content regulation specific to minors

---

## Content Adaptation Approach

### Level 1: Universal Content
Content appropriate across all jurisdictions with minimal adaptation.

**Example**: "Exercise benefits cardiovascular health."

**Adaptation Needed**: Minimal (possibly language/cultural framing adjustments)

---

### Level 2: Age-Gated Variation
Content appropriate across jurisdictions but with different age restrictions.

**Example**: Puberty education content

**Adaptation Needed**:
- Age restrictions vary by country
- Parental consent requirements vary
- Detail level may vary based on cultural norms

**Implementation**:
- Country profile determines age restrictions
- Content access controlled by country-specific rules
- Parental consent flow varies by jurisdiction

---

### Level 3: Culturally Adapted Content
Content requiring cultural adaptation while maintaining medical accuracy.

**Example**: Mental health condition literacy

**Adaptation Needed**:
- Stigma levels vary dramatically
- Communication approaches differ
- Family involvement expectations vary
- Help-seeking behavior cultural variation

**Implementation**:
- Core medical facts remain consistent
- Framing and language adapted
- Cultural context acknowledged
- Local resources and support systems referenced

---

### Level 4: Jurisdiction-Specific Content
Content that must be substantially different or unavailable in certain jurisdictions.

**Example**: 
- Reproductive healthcare information
- Gender-affirming care information
- Substance use harm reduction

**Adaptation Needed**:
- Legal restrictions may prohibit content entirely
- Medical guidelines vary significantly
- Cultural sensitivity required
- Legal consequences for inappropriate content delivery

**Implementation**:
- Geolocation-based content delivery
- Jurisdiction-specific versions
- Legal review for each major market
- Some content unavailable in certain countries

---

## Legal Variation Examples

### Age of Medical Consent
Varies dramatically worldwide:
- Some countries: Age 16 for all medical decisions
- Some countries: Age 18 for most decisions, lower for specific contexts
- Some countries: Parental consent always required for minors
- Some countries: "Mature minor" doctrine (capacity-based, not age-based)

**Content Impact**: 
- Affects when content can address independent medical decision-making
- Determines parental involvement requirements
- Influences tone and framing of medical information

---

### Restricted Topics by Jurisdiction

#### Reproductive Health
- **Highly Restrictive Jurisdictions**: Abortion information illegal or severely restricted
- **Moderately Restrictive**: Age restrictions, parental notification requirements
- **Permissive Jurisdictions**: Comprehensive information available with age-appropriate framing

**Content Approach**:
- Geolocation determines content availability
- Legal review for each jurisdiction
- Focus on medical facts where permitted
- Acknowledge legal variation explicitly

---

#### Gender-Affirming Healthcare
- **Restrictive Jurisdictions**: Discussion may be legally prohibited for minors
- **Moderately Restrictive**: Age restrictions, parental consent requirements
- **Permissive Jurisdictions**: Information available with safeguarding considerations

**Content Approach**:
- Jurisdiction-specific availability
- Legal review mandatory
- Medical consensus presented where legally permitted
- Safeguarding paramount regardless of jurisdiction

---

#### Mental Health and Self-Harm
- **Stigmatizing Contexts**: Mental health highly stigmatized, disclosure risky
- **Moderate Contexts**: Growing acceptance, resources developing
- **Supportive Contexts**: Open discussion, strong support systems

**Content Approach**:
- Universal safeguarding protocols
- Cultural framing adapted
- Resource availability acknowledged
- Stigma sensitivity in all contexts

---

## Cultural Adaptation Framework

### Communication Style

**Direct Cultures** (e.g., Northern Europe, North America in many contexts):
- Straightforward medical language
- Direct discussion of symptoms and conditions
- Individual decision-making emphasized

**Indirect Cultures** (e.g., many Asian, Middle Eastern, African contexts):
- More contextual medical language
- Family-centered decision-making acknowledged
- Respect for hierarchical medical relationships

**Content Approach**: Adapt communication style while maintaining medical accuracy.

---

### Family Involvement

**Individualistic Contexts**:
- Individual autonomy emphasized
- Independent medical decision-making for older teens

**Collectivist Contexts**:
- Family decision-making emphasized
- Multi-generational involvement expected

**Content Approach**: Acknowledge cultural variation in family involvement without imposing single model.

---

### Stigma and Mental Health

**High Stigma Contexts**:
- Mental health conditions highly stigmatized
- Disclosure risky
- Professional help-seeking discouraged culturally

**Lower Stigma Contexts**:
- Mental health openly discussed
- Professional help-seeking encouraged
- Strong support systems

**Content Approach**: 
- Acknowledge stigma variation
- Provide culturally appropriate support pathways
- Never shame help-seeking
- Protect confidentiality paramount

---

### Traditional Medicine Integration

**Strong Traditional Medicine Contexts**:
- Traditional medicine widely practiced
- Evidence-based and traditional medicine coexist
- Respect for traditional healers

**Evidence-Based Medicine Dominant Contexts**:
- Traditional medicine less prevalent
- Stronger distinction between evidence-based and traditional

**Content Approach**:
- Respect traditional practices
- Do not promote unproven treatments
- Acknowledge coexistence without false equivalence
- Maintain evidence-based foundation

---

## Implementation Strategy

### Tier 1 Countries (Launch Markets)
Full country profiles developed, extensive content adaptation.

**Selection Criteria**:
- Large user base (actual or potential)
- Clear legal framework
- Resources available for adaptation

**Implementation**:
- Complete country profile
- Legal review of all healthcare content
- Cultural adaptation where necessary
- Local resource integration

---

### Tier 2 Countries (Secondary Markets)
Country profiles developed, targeted content adaptation.

**Selection Criteria**:
- Significant user base
- Legal framework navigable

**Implementation**:
- Country profile (may be less detailed than Tier 1)
- Legal review of high-risk content
- Cultural adaptation for sensitive topics
- Generic resource information

---

### Tier 3 Countries (General Availability)
Basic country profile, minimal adaptation beyond age restrictions.

**Implementation**:
- Basic legal research
- Age restrictions applied
- Restricted topics blocked where legally required
- Generic resources only

---

## Enforcement Approach

### Geolocation-Based Controls
- User location determined via IP geolocation and/or device location
- Country-specific content rules applied automatically
- High-risk topics blocked in restrictive jurisdictions
- Age restrictions enforced per country profile

### VPN and Location Spoofing
- Acknowledge users may attempt to bypass geolocation
- Cannot prevent with 100% certainty
- Terms of service require honest location information
- Focus on good-faith compliance

### Legal Compliance
- Legal review for Tier 1 countries mandatory
- Legal consultation for Tier 2 countries recommended
- General legal principles applied to Tier 3 countries

### Cultural Sensitivity
- Cultural review for Tier 1 countries mandatory
- Cultural consultation for Tier 2 countries recommended
- General cultural principles applied to Tier 3 countries

---

## Country Profile Development Process

### Step 1: Country Selection
Governance lead identifies country for profile development (based on user base, strategic importance, resource availability).

### Step 2: Legal Research
Legal research conducted:
- Age of consent laws
- Healthcare content restrictions
- Data protection requirements
- Mandatory reporting obligations

### Step 3: Cultural Research
Cultural research conducted:
- Healthcare communication norms
- Stigmatized conditions
- Family involvement expectations
- Traditional medicine integration

### Step 4: Profile Creation
Country profile created using schema.

### Step 5: Content Review
Existing content reviewed against country profile, adaptations identified.

### Step 6: Implementation
Country-specific rules implemented in content delivery system.

### Step 7: Ongoing Monitoring
Country profile updated as laws and cultural norms evolve.

---

## Example Enforcement Scenarios

### Scenario 1: User in Restrictive Jurisdiction Accessing Reproductive Health Content
**Action**: Content blocked, message displayed acknowledging legal restrictions, generic health resources provided.

### Scenario 2: User in Stigmatizing Context Accessing Mental Health Content
**Action**: Content available, cultural framing adapted to reduce stigma, local resources provided where available, confidentiality emphasized.

### Scenario 3: User Below Age of Consent for Country
**Action**: Parental consent required, age-appropriate version provided if consent given, or access blocked if below minimum age even with consent.

---

## Related Documents

- `country_profile.schema.json` - Technical schema for country profiles
- `/examples/country_profiles/` - Example country profiles
- `HEALTHCARE_GOVERNANCE_PRINCIPLES.md` - Foundational principles
- `CULTURAL_ADAPTATION.md` - Implementation guide for cultural adaptation

---

## Review Cycle

This framework is reviewed:
- Annually
- When entering new major markets
- Upon significant legal changes in existing markets
- When cultural sensitivity concerns arise

Country profiles reviewed:
- Annually for Tier 1 countries
- Every 2 years for Tier 2 countries
- Every 3 years or as needed for Tier 3 countries

---

**Last Updated**: 2026-02-18  
**Next Review**: 2027-02-18  
**Document Owner**: Governance Lead  
**Version**: 1.0
