---
layout: default
title: Acyclovir
parent: Model Prediction Only (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
monitor_inn: "ACYCLOVIR"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "common wart", "post-infectious neuralgia", "hepatitis C induced liver cirrhosis", "eosinophilic pustular folliculitis", "sequela of COVID-19", "vulvovaginal candidiasis", "papular urticaria", "disease of orbital region", "epidemic keratoconjunctivitis"]
last_modified_at: 2026-10-14
description: "Acyclovir: predicted new indication Common wart (evidence level L5). Approved use: Herpes simplex infection, herpes zoster, chickenpox, herpes labialis…"
---

# Acyclovir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Acyclovir: From Herpesvirus Infections to Common Wart

## One-Sentence Summary

Acyclovir is an antiviral drug originally used to treat herpes simplex infections, herpes zoster (shingles), chickenpox, herpes labialis, herpes simplex encephalitis and genital herpes.
Among the model's top-ranked predictions, the one with the strongest supporting evidence is **Common Wart** (TxGNN rank 2; the rank 1 prediction has no relevant evidence). It is backed by **4 clinical trials** (up to Phase 2/3) and **20 publications**, including several small randomized comparative studies of intralesional acyclovir.
Evidence for the other top predictions is weak or absent.

> **Note on the lead prediction:** The top-scoring prediction, punctate epithelial keratoconjunctivitis (99.67%), has no clinical trials and only two unrelated case series (microsporidial keratoconjunctivitis and drug-induced corneal lipidosis). This report therefore focuses on common wart, the best-supported candidate, and summarizes the others briefly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes simplex infection, herpes zoster, chickenpox, herpes labialis, herpes simplex encephalitis, genital herpes |
| Predicted New Indication | Common wart (rank 2); rank 1 is punctate epithelial keratoconjunctivitis, which is unsupported (L5) |
| TxGNN Prediction Score | 99.46% (common wart); 99.67% (punctate epithelial keratoconjunctivitis) |
| Evidence Level | L2 (common wart) |
| US Market Status | Cancelled only (all licenses cancelled) |
| Number of NDAs | 16 (all cancelled; mostly ANDAs, with 1 NDA) |
| Recommended Decision | Proceed with Guardrails (as a research question; not ready for development) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for acyclovir are not available in the data compiled for this report. From general knowledge, acyclovir is a guanosine analogue that is selectively activated by viral thymidine kinase and then inhibits viral DNA polymerase, which explains its effect on herpesviruses.

Common warts are caused by human papillomavirus (HPV), a DNA virus. HPV does not encode thymidine kinase, so acyclovir's classical selective activation is not expected to work. Proposed alternatives include non-selective uptake with inhibition of viral DNA polymerase, local immune stimulation, and an inflammatory response triggered by intralesional injection. The mechanism remains uncertain.

Despite this, the clinical signal is real. Several small randomized comparisons report responses to intralesional acyclovir, and a Phase 2/3 randomized trial against cryotherapy in plantar warts has been published in a major dermatology journal. The prediction is therefore plausible as a research question, though not yet established.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06261684](https://clinicaltrials.gov/study/NCT06261684) | Phase 2/3 | Unknown | 92 | Randomized trial of intralesional acyclovir vs cryotherapy in plantar warts (safety and efficacy); corresponding publication is PMID 40889709 |
| [NCT05429151](https://clinicaltrials.gov/study/NCT05429151) | Phase 4 | Unknown | 40 | Intralesional acyclovir (70 mg/ml, every 2 weeks) vs Candida antigen in plantar warts, with dermoscopic assessment |
| [NCT07448844](https://clinicaltrials.gov/study/NCT07448844) | Phase 4 | Recruiting | 40 | Intralesional vitamin D3 vs acyclovir in common, plantar, flat and periungual warts; primary endpoint is complete clearance at week 8 |
| [NCT05324904](https://clinicaltrials.gov/study/NCT05324904) | N/A | Unknown | 44 | Intralesional vitamin D3 vs acyclovir in plantar warts, comparing efficacy and safety |

All four trials are small, and three have unknown status.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40889709](https://pubmed.ncbi.nlm.nih.gov/40889709/) | 2026 | RCT | J Am Acad Dermatol | Intralesional acyclovir vs cryotherapy in plantar warts |
| [40488756](https://pubmed.ncbi.nlm.nih.gov/40488756/) | 2025 | RCT/Comparative | Arch Dermatol Res | Intralesional acyclovir vs intralesional 5-FU in recalcitrant warts |
| [40056255](https://pubmed.ncbi.nlm.nih.gov/40056255/) | 2025 | RCT/Comparative | Arch Dermatol Res | Intralesional acyclovir vs quadrivalent HPV vaccine in 60 patients with recalcitrant warts |
| [38822848](https://pubmed.ncbi.nlm.nih.gov/38822848/) | 2024 | RCT | Arch Dermatol Res | Intralesional acyclovir vs hepatitis B vaccine in resistant plantar warts (48 patients completed) |
| [41686619](https://pubmed.ncbi.nlm.nih.gov/41686619/) | 2026 | Systematic review / network meta-analysis | Medicine | Compares treatments for cutaneous warts; intralesional acyclovir is described as a novel option |
| [37303436](https://pubmed.ncbi.nlm.nih.gov/37303436/) | 2023 | Comparative study | Cureus | Intralesional acyclovir vs PPD immunotherapy in viral warts |
| [34412535](https://pubmed.ncbi.nlm.nih.gov/34412535/) | 2022 | Clinical study | J Cutan Med Surg | Intralesional acyclovir as a potential option for cutaneous warts |
| [38793636](https://pubmed.ncbi.nlm.nih.gov/38793636/) | 2024 | Case reports and review | Viruses | Remission of HPV-related disease (e.g., penile condyloma) with acyclovir or valacyclovir |
| [26885794](https://pubmed.ncbi.nlm.nih.gov/26885794/) | 2016 | Case report | J Drugs Dermatol | Persistent plantar warts resolved after a 10-day course of oral acyclovir given for herpes zoster |
| [6467981](https://pubmed.ncbi.nlm.nih.gov/6467981/) | 1984 | Report | Cutis | Acyclovir ointment in verrucae vulgares |

The remaining retrieved publications are general reviews (STI, HIV oral lesions, pregnancy skin infections) with little acyclovir-specific evidence on warts.

---

## US Market Information

All 16 US licenses are cancelled; none is currently valid. Representative entries (several are valacyclovir products, the prodrug):

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA020487 | VALTREX (GlaxoSmithKline) | Film-coated tablet | Not listed |
| ANDA075382 | Acyclovir (Golden State Medical Supply) | Tablet | Not listed |
| ANDA074889 | Acyclovir (Major Pharmaceuticals) | Capsule | Not listed |
| ANDA074930 | Acyclovir (Fresenius Kabi) | Injection, solution | Not listed |
| ANDA212361 | Acyclovir (Alembic) | Cream | Not listed |

Dosage forms across all licenses include oral tablets and capsules, injectable solution, ointment and cream.

---

## Safety Considerations

No label-based warnings or contraindications were available in the data compiled for this report. Please refer to the package insert for safety information.

Additional information that is available:

- **Knowledge-graph contraindication signals** (not label text, so interpret cautiously): kidney disease and impaired renal function, hemolytic-uremic syndrome, thrombocytopenic purpura, hypertension, diabetes and hyperglycemia, cerebrovascular and cardiovascular disease (stroke, myocardial infarction), peripheral vascular disease, and adrenal insufficiency, among others.
- **Drug interactions** (100 interactions recorded; moderate-level ones shown): balsalazide, mesalazine, olsalazine, sulfasalazine and trospium. Others have an unknown severity level, including amphotericin B, mannitol, metformin, morphine and several proton pump inhibitors.

---

## Other Predicted Indications (Brief Summary)

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Punctate epithelial keratoconjunctivitis | 99.67% | L5 | No relevant evidence; retrieved literature is non-herpetic. Hold |
| Post-infectious neuralgia | 99.25% | L5 | No trials or literature. Hold |
| Hepatitis C-induced cirrhosis | 99.23% | L5 | Acyclovir has no known anti-HCV activity. Hold |
| Eosinophilic pustular folliculitis | 99.22% | L5 | No plausible antiviral mechanism. Hold |
| Sequela of COVID-19 | 99.16% | L4 | Only indirect evidence (treating herpesvirus reactivation). Hold |
| Vulvovaginal candidiasis | 99.11% | L5 | Candida is a fungus; likely a herpes genitalis association artifact. Hold |
| Papular urticaria | 99.09% | L5 | No trials or literature. Hold |
| Disease of orbital region | 99.08% | L2 | Mostly reflects existing herpetic eye use, not true repurposing; trials are small. Research question |
| Epidemic keratoconjunctivitis | 99.07% | L4 | Caused mainly by adenovirus, which acyclovir does not effectively inhibit. Hold |

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for common wart, as a research question only)

**Rationale:**
Common wart is the only predicted indication with randomized evidence that directly tests acyclovir, including a Phase 2/3 trial and several small comparative studies. The mechanism is uncertain because HPV lacks thymidine kinase, the trials are small and mostly single-center with unknown status, and no US licenses are currently valid. The remaining predictions should be held.

**To proceed, the following is needed:**
- Larger, well-controlled confirmatory trials with a placebo or standard-of-care comparator, and long-term recurrence follow-up
- Clarification of the mechanism of action, including mechanism of action data for acyclovir
- FDA package insert warnings and contraindications (currently missing and flagged as a blocking gap for safety screening)
- A defined regulatory route for intralesional use, since the existing products are oral, injectable, and topical, and no product is labeled for intralesional wart treatment
- Safety evaluation for intralesional administration, including renal considerations given the knowledge-graph signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

