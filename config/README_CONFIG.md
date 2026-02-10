# Platform Cultural Configuration

This folder defines the governing logic for how the platform handles:
- **time**
- **region**
- **genre**
- **premieres**
- **festivals**

These files are the **single source of truth** for cultural rhythm and curation.

**Developers must never hard-code time, region, or genre logic in the application.**

All systems should read from these configs.

---

## 1. Time — Annual Release Calendar

**Defined in `release_calendar.yaml`**

- The year is divided into **26 fortnights**, each with **26 films**.
- Each month contains **4 premieres**.
- This creates a predictable cultural rhythm:
  - fortnightly waves
  - weekly premieres
  - monthly regional spotlights

**All scheduling logic must reference this file.**

---

## 2. Genre — Rotation Schedule

**Defined in `genre_rotation.yaml`**

- **10 core genres**.
- **5 featured genres per fortnight**.
- **No consecutive repeats**.
- Minimum and maximum annual appearances ensure balance.

**Curation engines must use this rotation, not algorithmic popularity.**

---

## 3. Region — Spotlight Cycle

**Defined in `regions.yaml`**

- Each quarter highlights **3 regions**.
- Each month has a **single spotlight region**.
- This ensures global balance and prevents cultural dominance.

**Regional availability, pricing, and curation must reference this file.**

---

## 4. Premiere — Ceremony Structure

**Defined in `premiere_structure.yaml`**

A premiere is a **ritual**, not a content drop.

- **Announcement** (T-7)
- **Artist introduction** (T-1)
- **Premiere window** (T to T+3)
- **Reflection phase** (T+3 to T+7)
- **Archive & rotation**

**UI and notifications must follow this structure.**

---

## 5. Festivals — Integration Pipeline

**Defined in `festivals.yaml`**

- Intake windows
- Regional mapping
- Annual caps
- Balance rules

**Festival films must be scheduled into the release calendar without breaking cadence.**

---

## Purpose of This Folder

This folder ensures:
- **cultural consistency**
- **global fairness**
- **predictable rhythm**
- **transparent governance**
- **developer clarity**

**It is the cultural constitution of the platform.**