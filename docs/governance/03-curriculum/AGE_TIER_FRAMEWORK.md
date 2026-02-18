# Age-Tier Framework

## Overview

The **Age-Tier Framework** ensures that all learning content is matched to cognitive development, emotional maturity, and safeguarding needs.

This framework is **principle-based**, not prescriptive. It provides guidance for curriculum design while allowing flexibility for cultural context and individual learner needs.

---

## 1. Purpose

The Age-Tier Framework exists to ensure that:

- content is cognitively appropriate
- emotional demands match learner resilience
- abstract reasoning is scaffolded appropriately
- exposure risks are minimized
- consent boundaries are respected
- neutrality requirements are upheld

This framework protects learners while enabling rich, age-appropriate learning experiences.

---

## 2. Age-Tier Principles

Each tier must consider:

### 2.1 Cognitive Load
- Is the content mentally accessible to learners in this tier?
- Does it require abstract reasoning beyond the learner's developmental stage?
- Is scaffolding provided for complex concepts?

### 2.2 Emotional Resilience
- Can learners in this tier process the emotional content safely?
- Does the content risk overwhelming or distressing learners?
- Are support mechanisms in place if the content is challenging?

### 2.3 Abstract Reasoning Ability
- Can learners in this tier distinguish between literal and metaphorical content?
- Can they engage with nuance, ambiguity, and multiple perspectives?
- Is the content concrete enough for their developmental stage?

### 2.4 Exposure Risk
- Does the content expose learners to harmful ideas, images, or influences?
- Could the content be misinterpreted or misused?
- Are safeguarding measures embedded?

### 2.5 Consent Boundaries
- Does this content require parental or guardian consent?
- Are learners able to give informed consent (where appropriate)?
- Are opt-out mechanisms available?

### 2.6 Neutrality Requirements
- Is the content free from ideological persuasion?
- Are contested topics presented with balanced framing?
- Does the content distinguish fact, interpretation, and opinion?

---

## 3. Age-Tier Schema

The schema defines **what must be captured** for each age tier, not the content itself.

```yaml
age_tier:
  id: string                                  # Unique identifier (e.g., "tier_1", "tier_primary")
  label: string                               # Human-readable name (e.g., "Early Years", "Primary")
  min_age: integer                            # Minimum age in years
  max_age: integer                            # Maximum age in years
  cognitive_profile: string                   # Description of cognitive capabilities
  permitted_content_categories: [string]      # Categories allowed for this tier
  restricted_content_categories: [string]     # Categories restricted for this tier
  parental_consent_required: boolean          # Whether parental consent is mandatory
  notes: string                               # Additional context or guidance
```

### Example (Illustrative, Not Prescriptive)

```yaml
age_tier:
  id: "tier_primary"
  label: "Primary (Ages 5-11)"
  min_age: 5
  max_age: 11
  cognitive_profile: "Developing concrete reasoning; limited abstract thinking; high curiosity; emotionally vulnerable."
  permitted_content_categories:
    - "foundational_literacy"
    - "basic_numeracy"
    - "creative_expression"
    - "social_emotional_learning"
  restricted_content_categories:
    - "political_content"
    - "graphic_history"
    - "mature_themes"
  parental_consent_required: true
  notes: "Content must be concrete, emotionally safe, and scaffolded for early learners."
```

For the full JSON schema definition, see [age_tier.schema.json](../schemas/age_tier.schema.json).

---

## 4. Tier Flexibility

Age tiers are **guidance**, not rigid gates.

The Curriculum Council may adjust tiers based on:

### 4.1 Cultural Context
- Some communities may have different expectations for age-appropriate content
- Cultural norms around childhood development vary
- The framework adapts to respect diverse perspectives while maintaining safeguarding standards

### 4.2 Developmental Research
- As understanding of child development evolves, tiers may be refined
- Neuroscience and educational psychology inform tier boundaries
- Tiers are updated in response to evidence, not ideology

### 4.3 Safeguarding Advisories
- If new risks are identified, tiers may be adjusted to protect learners
- The Safeguarding Board may recommend changes to tier boundaries
- Safety always takes precedence over content delivery

### 4.4 Individual Learner Needs
- Some learners may be ready for content earlier or later than their age suggests
- Parental discretion and educator judgment may allow flexibility
- Tier boundaries are defaults, not absolute barriers

---

## 5. Implementation Guidance

### 5.1 Curriculum Design
When designing curriculum:

1. Identify the target age tier
2. Review cognitive and emotional requirements
3. Ensure content aligns with permitted categories
4. Avoid restricted categories
5. Embed scaffolding and support mechanisms
6. Include consent requirements where applicable

### 5.2 Content Review
When reviewing content:

1. Assess cognitive load
2. Evaluate emotional resilience demands
3. Check for exposure risks
4. Verify neutrality
5. Confirm age-tier alignment
6. Document rationale for tier assignment

### 5.3 Escalation
If content falls in a gray area:

- Escalate to the Curriculum Council for review
- Involve the Safeguarding Board if risk is present
- Document the decision with clear rationale

---

## 6. Consent Integration

Age tiers are integrated with the [Consent Status Schema](../schemas/consent_status.schema.json).

Certain tiers require:

- parental or guardian consent before access
- opt-in mechanisms for sensitive content
- clear disclosure of content nature

This ensures learners and families have agency over their learning experience.

---

## 7. Relationship to Other Frameworks

The Age-Tier Framework works alongside:

- **Curriculum Council Mandate** — the governing body that maintains this framework
- **Instructor Code of Conduct** — instructors must respect tier boundaries
- **Curriculum Authorship & Neutrality** — content must align with tier-appropriate neutrality standards
- **Consent Status Schema** — consent flows are informed by tier requirements

---

## 8. Review Cycle

The Age-Tier Framework is reviewed:

- annually
- upon significant changes in developmental research
- when safeguarding advisories are issued
- when community feedback raises valid concerns

---

## 9. Contact

For Age-Tier Framework inquiries:

- [Contact details to be added]

---

**This framework is designed to last decades. It provides principles, not prescriptions.**

---

## Related Documents

- [Curriculum Council Mandate](CURRICULUM_COUNCIL_MANDATE.md)
- [Instructor Code of Conduct](INSTRUCTOR_CODE_OF_CONDUCT.md)
- [Curriculum Authorship & Neutrality](CURRICULUM_AUTHORSHIP_NEUTRALITY.md)
- [Age Tier Schema](../schemas/age_tier.schema.json)
- [Consent Status Schema](../schemas/consent_status.schema.json)
