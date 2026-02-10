# Configuration System Documentation

This folder contains the core configuration files that drive the John T Hope platform's content scheduling, curation, and premiere orchestration.

## 📁 Folder Structure

```
config/
├── release_calendar.yaml       # Annual release schedule (fortnights & premieres)
├── genre_rotation.yaml         # Genre diversity and rotation rules
├── regions.yaml                # Regional spotlight cycle
├── premiere_structure.yaml     # Premiere ceremony phases and rituals
├── festivals.yaml              # Festival integration pipeline
└── README_CONFIG.md            # This documentation file
```

## 🎯 System Overview

The John T Hope platform uses a **config-driven architecture** where all scheduling, curation, and premiere logic reads from YAML configuration files rather than hard-coded values. This enables:

- **Predictable cadence**: 26 fortnights, 676 films, 48 premieres per year
- **Dynamic diversity**: Genre rotation and regional spotlights
- **Ritual premieres**: Structured ceremony phases, not just "content drops"
- **Festival integration**: Systematic intake from global festivals

This keeps all cultural logic centralised, version-controlled, and transparent.

## 📄 Configuration Files

### 1. `release_calendar.yaml`
**Purpose**: Defines the annual release calendar with fortnightly waves and monthly premieres.

**Key Data**:
- 26 fortnights (F1-F26) with start/end dates
- 26 films per fortnight = 676 films/year
- 4 premieres per month = 48 premieres/year

**Used By**:
- Scheduling system
- Content management UI
- Premiere orchestration
- Analytics dashboard

---

### 2. `genre_rotation.yaml`
**Purpose**: Manages genre diversity across fortnightly film waves.

**Key Data**:
- 10 genres: Drama, Comedy, Documentary, World Cinema, Experimental, Animation, Thriller, Romance, Political, Art House
- 5 featured genres per fortnight
- Rules: No consecutive repeats, 4-10 appearances per year per genre

**Used By**:
- Curatorial selection tools
- Homepage featured genres
- Film recommendation engine
- Festival intake evaluation

**Logic**: Each fortnight, 5 "featured genres" are selected according to rotation rules. Pages read from this config, not hard-coded choices.

---

### 3. `regions.yaml`
**Purpose**: Establishes the regional spotlight cycle for global cinema balance.

**Key Data**:
- 7 regions: Africa, Europe, Asia, Latin America, North America, Middle East, Oceania
- Quarterly balance: Each quarter cycles through 3 regions
- Monthly spotlight: 1 region per month, repeats twice yearly

**Used By**:
- Homepage regional spotlight section
- Festival film prioritization
- Curatorial balance tracking
- Marketing campaigns

**Logic**: UI and curation logic read this to decide which region gets priority in any given month.

---

### 4. `premiere_structure.yaml`
**Purpose**: Defines the premiere ceremony ritual with fixed phases.

**Key Data**:
- 5 phases: Announcement (T-7), Artist Introduction (T-1), Premiere Window (T to T+3), Reflection (T+3 to T+7), Archive (T+7+)
- Channel orchestration: homepage, email, social
- Features: live chat, moment capture, Q&A

**Used By**:
- Premiere automation workflows
- Marketing automation
- Email campaign scheduler
- Homepage banner system

**Logic**: This lets devs build flows around a fixed ceremony pattern. A premiere is not "content goes live"; it's a ritual.

---

### 5. `festivals.yaml`
**Purpose**: Manages festival film intake pipeline with rules and workflow.

**Key Data**:
- 9 global festivals with intake windows and film caps
- Pipeline rules: 30% A-list cap, 40% under-represented minimum
- 5-step workflow: Identification → Selection → Scheduling → Rights → Premiere

**Used By**:
- Festival intake management tools
- Curatorial scheduling system
- Rights management tracking
- Festival partner dashboards

**Workflow**:
1. **Festival Identification**: Festival identifies candidate films
2. **Curatorial Selection**: Team selects based on region, genre, and balance
3. **Calendar Scheduling**: Films slotted respecting genre rotation, regional spotlight, premiere capacity (4/month)
4. **Rights Confirmation**: Contracts + rights confirmed
5. **Premiere Ceremony**: Structure applied

---

## 🔗 System Integration

All configuration files work together to create a cohesive programming system:

```
Festival Films → Genre Rotation → Regional Spotlight → Release Calendar → Premiere Ceremony
```

**Example Flow**:
1. Sundance identifies 20 candidate films (North America region)
2. Curatorial team selects 8 films across various genres
3. Films scheduled into February-March fortnights (North America is spotlight in Q1)
4. Genre rotation ensures no consecutive Drama weeks
5. Each film gets full premiere ceremony treatment (T-7 to T+7)
6. Monthly premiere cap of 4 is respected

---

## 🎨 Usage for Developers

### Reading Configurations

```python
import yaml

# Load release calendar
with open('config/release_calendar.yaml', 'r') as f:
    calendar = yaml.safe_load(f)
    
# Get current fortnight
current_fortnight = calendar['fortnights'][0]
print(f"Fortnight {current_fortnight['id']}: {current_fortnight['start']} to {current_fortnight['end']}")

# Load genre rotation
with open('config/genre_rotation.yaml', 'r') as f:
    genres = yaml.safe_load(f)
    
# Get featured genres for current fortnight
featured_genres = get_featured_genres(genres, current_fortnight['id'])
```

### Validating Against Rules

```python
def validate_premiere_capacity(month, scheduled_premieres):
    """Ensure no more than 4 premieres per month"""
    if len(scheduled_premieres) > 4:
        raise ValueError(f"Month {month} exceeds premiere capacity (4 max)")
    return True

def validate_genre_rotation(fortnight_id, selected_genre):
    """Ensure no consecutive genre repeats"""
    previous_fortnight = get_previous_fortnight(fortnight_id)
    if selected_genre in previous_fortnight['featured_genres']:
        raise ValueError(f"Genre {selected_genre} was featured in previous fortnight")
    return True
```

---

## 📊 Configuration Validation

Before updating any configuration file, validate it against these rules:

### Release Calendar
- ✅ Exactly 26 fortnights per year
- ✅ No date overlaps between fortnights
- ✅ 48 total premieres (4 per month × 12 months)

### Genre Rotation
- ✅ All genres appear 4-10 times per year
- ✅ No genre repeats in consecutive fortnights
- ✅ 5 genres featured per fortnight × 26 fortnights = 130 slots

### Regional Spotlight
- ✅ Each quarter has 3 different regions
- ✅ All 7 regions appear at least once per year
- ✅ Monthly spotlight assignments cover all 12 months

### Festival Integration
- ✅ No festival exceeds its max_films_per_year
- ✅ No more than 30% of premieres from A-list festivals
- ✅ At least 40% from under-represented regions

---

## 🚀 Updating Configurations

To update any configuration:

1. **Edit the YAML file** in `config/` folder
2. **Run validation script**: `python scripts/validate_config.py`
3. **Test in staging environment**
4. **Commit changes** with descriptive message
5. **Deploy to production**

**Example commit message**:
```
Update genre_rotation.yaml: Add Korean Cinema genre for 2027 Q3
```

---

## 🎬 Example Scenarios

### Scenario 1: Adding a New Festival
Edit `festivals.yaml`:
```yaml
- id: rotterdam
  name: "International Film Festival Rotterdam"
  region: "Europe"
  intake_window: "2027-02-01 to 2027-03-31"
  max_films_per_year: 10
```

### Scenario 2: Adjusting Genre Balance
Edit `genre_rotation.yaml`:
```yaml
rotation:
  fortnight_slots: 6  # Increased from 5
  rules:
    - minimum_appearances_per_year: 5  # Increased from 4
```

### Scenario 3: Changing Regional Focus
Edit `regions.yaml`:
```yaml
monthly_spotlight:
  1: Asia  # Changed from Africa
  2: Africa  # Changed from Europe
  # ... continue adjustments
```

---

## 📖 Additional Resources

- **Platform Architecture**: See main `README.md`
- **API Documentation**: `/docs/api.md`
- **Curatorial Guidelines**: `/docs/curation.md`
- **Premiere Automation**: `/docs/automation.md`

---

## 💡 Philosophy

This configuration system embodies the John T Hope platform's core values:

- **Transparency**: All rules are visible and documented
- **Predictability**: Fixed cadence and structure
- **Diversity**: Enforced through genre and regional rotation
- **Ritual**: Premieres as ceremonies, not content drops
- **Balance**: Data-driven curation decisions

---

**Last Updated**: 2026-02-10 19:56:57  
**Maintained By**: John T Hope Platform Team
