# DRPALL DR20 Summary Table

## Metadata

- **AUTHOR:** S.F. Sanchez  
- **SOURCE:** LVM DR20 DRP summary table  
- **DATE:** 2026-XX-XX  
- **VERSION:** DR20 v1.2.0  
- **COLAPRV:** S.F. Sanchez  
- **PUBAPRV:**  

## Description

The file `drpall_DR20.fits` is a summary table produced by the LVM Data Reduction Pipeline (DRP) that compiles observational, instrumental, and processing metadata for each science exposure included in DR20; each row corresponds to an individual exposure (identified by `tileid`, `mjd`, and `expnum`) and contains detailed information on telescope pointing, observing conditions, and instrument configuration for the science field (SCI) and associated sky fields (SKYE and SKYW), including astrometry, airmass, altitude, focus metrics, and angular separations from the Moon, as well as lunar and solar conditions at the time of observation; in addition, it records pipeline-related information such as reduction stage, processing status, quality flags, DRP version, calibration references, and file locations, thereby providing a comprehensive master catalog to track data provenance, assess data quality, and enable the selection and filtering of LVM DR20 observations for scientific analysis. :contentReference[oaicite:0]{index=0}

---

## Columns

### General Information

| Column | Name     | Type   | Units   | Description |
|--------|----------|--------|---------|-------------|
| 1 | tilegrp | string | | Tile group identifier |
| 2 | tileid | int | | Unique tile identifier |
| 3 | mjd | int | | Modified Julian Date of the observation |
| 4 | expnum | int | | Exposure number within the observing sequence |
| 5 | exptime | float | seconds | Exposure time |
| 6 | stage | int | | Reduction stage identifier |
| 7 | status | int | | Processing status flag |
| 8 | drpqual | int | | DRP quality flag |
| 9 | drpver | string | | Version of the DRP used |
| 10 | dpos | int | | Dither position index |
| 11 | object | string | | Object or field name |
| 12 | obstime | string | | Observation timestamp |

---

### Science Field (SCI)

| Column | Name | Type | Units | Description |
|--------|------|------|-------|-------------|
| 13 | sci_ra | float | degree | Right Ascension of science pointing |
| 14 | sci_dec | float | degree | Declination of science pointing |
| 15 | sci_pa | float | degree | Position angle of science field |
| 16 | sci_amass | float | | Airmass of science exposure |
| 17 | sci_kmpos | float | | KM mirror position |
| 18 | sci_focpos | float | | Focus position |
| 19 | sci_alt | float | degree | Altitude of science pointing |
| 20 | sci_sh_hght | float | | Shack-Hartmann height or focus metric |
| 21 | sci_moon_sep | float | degree | Angular separation to the Moon |

---

### East Sky Field (SKYE)

| Column | Name | Type | Units | Description |
|--------|------|------|-------|-------------|
| 22 | skye_ra | float | degree | RA of eastern sky field |
| 23 | skye_dec | float | degree | DEC of eastern sky field |
| 24 | skye_pa | float | degree | Position angle of sky field |
| 25 | skye_amass | float | | Airmass of sky field |
| 26 | skye_kmpos | float | | KM mirror position for sky |
| 27 | skye_focpos | float | | Focus position for sky |
| 28 | skye_name | string | | Identifier of sky field |
| 29 | skye_alt | float | degree | Altitude of sky field |
| 30 | sci_skye_sep | float | degree | Separation SCI–SKYE |
| 31 | skye_sh_hght | float | | Focus metric for sky field |
| 32 | skye_moon_sep | float | degree | Separation sky–Moon |

---

### West Sky Field (SKYW)

| Column | Name | Type | Units | Description |
|--------|------|------|-------|-------------|
| 33 | skyw_ra | float | degree | RA of western sky field |
| 34 | skyw_dec | float | degree | DEC of western sky field |
| 35 | skyw_pa | float | degree | Position angle of sky field |
| 36 | skyw_amass | float | | Airmass of sky field |
| 37 | skyw_kmpos | float | | KM mirror position for sky |
| 38 | skyw_focpos | float | | Focus position for sky |
| 39 | skyw_name | string | | Identifier of sky field |
| 40 | skyw_alt | float | degree | Altitude of sky field |
| 41 | sci_skyw_sep | float | degree | Separation SCI–SKYW |
| 42 | skyw_sh_hght | float | | Focus metric for sky field |
| 43 | skyw_moon_sep | float | degree | Separation sky–Moon |

---

### Moon / Sun Conditions

| Column | Name | Type | Units | Description |
|--------|------|------|-------|-------------|
| 44 | moon_ra | float | degree | RA of the Moon |
| 45 | moon_dec | float | degree | DEC of the Moon |
| 46 | moon_phase | float | | Moon phase (fraction illuminated) |
| 47 | moon_fli | float | | Fractional lunar illumination |
| 48 | sun_alt | float | degree | Altitude of the Sun |
| 49 | moon_alt | float | degree | Altitude of the Moon |

---

### File and Calibration Metadata

| Column | Name | Type | Units | Description |
|--------|------|------|-------|-------------|
| 50 | filename | string | | Name of the reduced file |
| 51 | location | string | | File system location |
| 52 | agcam_location | string | | Acquisition camera data location |
| 53 | calib_mjd | int | | Calibration MJD used |

---

### Target Reference Coordinates

| Column | Name | Type | Units | Description |
|--------|------|------|-------|-------------|
| 54 | ra | float | degree | Reference RA of the target |
| 55 | dec | float | degree | Reference DEC of the target |
| 56 | pa | float | degree | Reference position angle |

---

### Object Identification

| Column | Name | Type | Units | Description |
|--------|------|------|-------|-------------|
| 57 | NGCname | string | | NGC identifier if available |

---

### Coordinate Systems

| Column | Name | Type | Units | Description |
|--------|------|------|-------|-------------|
| 58 | ra_icrs | float | degree | RA in ICRS frame |
| 59 | dec_icrs | float | degree | DEC in ICRS frame |
| 60 | ra_g | float | degree | Galactic longitude |
| 61 | dec_g | float | degree | Galactic latitude |