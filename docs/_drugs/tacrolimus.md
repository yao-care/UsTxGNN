---
layout: default
title: Tacrolimus
parent: Model Prediction Only (L5)
nav_order: 1191
evidence_level: L5
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tacrolimus: From Established Topical Immunomodulator Use to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor, and its ointment form is a well-established topical treatment for atopic dermatitis. The TxGNN model predicts it may be effective for **seborrheic dermatitis**, with **2 clinical trials** (1 completed Phase 3, 1 completed Phase 4) and **20 publications** supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the supplied record (approved indication text is empty for all licenses) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L2 (see note below) |
| US Market Status | ✓ Marketed |
| Number of NDAs | 20 licenses (NDA and ANDA combined) |
| Recommended Decision | Proceed with Guardrails |

> **Evidence level note:** Under the rules used here, L1 needs at least 2 completed Phase 3 RCTs. Only one completed Phase 3 trial (NCT02004860) targets seborrheic dermatitis, plus one Phase 4 study, so this report assigns L2. The source pipeline labelled it L1.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. From general pharmacology and the retrieved literature, tacrolimus inhibits calcineurin, which suppresses T-cell activation and the release of IL-2 and other pro-inflammatory cytokines. Reviews of tacrolimus ointment describe this as its primary mechanism in inflammatory skin disease.

Seborrheic dermatitis is a chronic, relapsing inflammatory skin disease that mainly affects the face and scalp. Its inflammatory component is linked to the skin's response to *Malassezia* yeast. Topical tacrolimus is already established for another inflammatory dermatitis, atopic dermatitis. This makes it a mechanistically plausible option for seborrheic dermatitis.

It is also a steroid-sparing choice. Long-term topical corticosteroids on facial skin risk atrophy, which is a main reason calcineurin inhibitors are studied for facial seborrheic dermatitis. Trials so far focus on maintenance therapy to prolong remission and reduce relapses.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Protopic (tacrolimus) ointment as maintenance treatment of severe seborrheic dermatitis on the adult face. Aim is to prolong remission and reduce relapses and topical steroid use. Primary outcome results were not in the supplied data. |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive use of 0.1% tacrolimus ointment once or twice weekly in adult facial seborrheic dermatitis, testing whether it keeps remission and reduces exacerbations. Results were not in the supplied data. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | RCT (multicenter, double-blind) | J Am Acad Dermatol | Tacrolimus 0.1% vs ciclopirox 1% as maintenance therapy in severe facial seborrheic dermatitis. |
| [22101215](https://pubmed.ncbi.nlm.nih.gov/22101215/) | 2012 | RCT (single-blind) | J Am Acad Dermatol | Hydrocortisone 1% ointment vs tacrolimus 0.1% ointment for facial seborrheic dermatitis in adults. |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Comparative study | Indian J Dermatol Venereol Leprol | Oral itraconazole for two days plus topical tacrolimus vs topical tacrolimus alone for maintenance treatment in Vietnam. |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Clinical trial | Ann Parasitol | Sertaconazole 2% cream vs tacrolimus 0.03% cream in 60 patients. |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical study | Ann Dermatol | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment. |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open pilot study | J Am Acad Dermatol | 18 patients treated with 0.1% tacrolimus for up to 28 days. 11 (61%) reached 100% clearance. |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | Am J Clin Dermatol | Topical treatments for facial seborrheic dermatitis. Covers antifungals, keratolytics and corticosteroids. |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Topical calcineurin inhibitors in seborrheic dermatitis. Describes them as a safe alternative to corticosteroids, which have limited long-term use. |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Current status and therapeutic horizons for facial seborrheic dermatitis. |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | Topical tacrolimus and pimecrolimus, including published experience in seborrheic dermatitis and other skin disorders. |

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA090687 | Tacrolimus (Cardinal Health 107, LLC) | Capsule | Not listed in supplied record |
| ANDA200744 | Tacrolimus (E. Fougera & Co.) | Ointment | Not listed in supplied record |
| NDA050777 | Tacrolimus (Padagis Israel Pharmaceuticals Ltd) | Ointment | Not listed in supplied record |
| ANDA065461 | Tacrolimus (Proficient Rx LP) | Capsule | Not listed in supplied record |
| ANDA090802 | Tacrolimus (Panacea Biotec Limited) | Capsule, gelatin coated | Not listed in supplied record |

Of the 20 licenses, the record lists these 5. It also shows extended-release capsules among the dosage forms. The predicted indication is topical, and ointment products are already marketed in the US (ANDA200744, NDA050777), so the route is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 trial and one completed Phase 4 study in adult facial seborrheic dermatitis, plus a randomized comparative trial in the literature, directly support tacrolimus ointment as maintenance therapy. The mechanism is plausible and the ointment form is already on the US market. The safety data are missing from the record, so the decision stays at guardrails rather than an unconditional Go.

**To proceed, the following is needed:**
- Package insert warnings and contraindications, which are currently missing and block the safety screening.
- Mechanism of action data from DrugBank (DB00864) to confirm the mechanistic link.
- Primary outcome results for NCT02004860 and NCT01591070, including relapse rates and tolerability.
- The approved indication text for the US ointment labels, to confirm whether seborrheic dermatitis use is on-label or off-label.
- A safety monitoring plan for long-term or repeated facial application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

