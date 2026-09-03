---
layout: default
title: Sulfadiazine
parent: 僅模型預測 (L5)
nav_order: 1186
evidence_level: L5
indication_count: 2
---

# Sulfadiazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sulfadiazine: From Bacterial Infections to Pneumocystosis

## One-Sentence Summary

> Sulfadiazine is a sulfonamide antibacterial; its formally documented original indication is not available in this evidence pack (mechanism of action is also marked as a data gap).
> The TxGNN model predicts it may be effective for **Pneumocystosis**,
> with **0 clinical trials** and **20 publications** currently supporting this direction, though the strongest data are historical case series/case reports rather than controlled trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (data gap — drug is classified as a sulfonamide antibacterial, but no approved indication text is present in this evidence pack) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.39% |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Licenses | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Sulfadiazine is a sulfonamide-class antimicrobial; its efficacy — particularly in combination with pyrimethamine — is well documented in the treatment of toxoplasmic encephalitis in AIDS patients, and mechanistically may be applicable to Pneumocystosis.

Sulfadiazine inhibits pathogen dihydropteroate synthase (DHPS), blocking the folate synthesis pathway. This is the same mechanistic class as the current standard-of-care for PCP, trimethoprim-sulfamethoxazole (sulfamethoxazole is also a sulfonamide). Historical literature shows sulfadiazine, when combined with pyrimethamine, has mainly been used to treat toxoplasmic encephalitis in AIDS patients, and has been used as a treatment/prophylaxis option in immunocompromised patients with concurrent *Pneumocystis carinii* (now *P. jirovecii*) pneumonia.

The mechanistic link is plausible but is drawn largely from combination-therapy contexts (sulfadiazine + pyrimethamine treating concurrent toxoplasmosis and PCP), rather than direct evidence of sulfadiazine monotherapy for PCP. This distinction should be kept in mind when interpreting the prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2645082](https://pubmed.ncbi.nlm.nih.gov/2645082/) | 1989 | Case Series | Clinical Pharmacy | Pyrimethamine-sulfadiazine used for treating PCP and toxoplasmosis in AIDS patients |
| [5315969](https://pubmed.ncbi.nlm.nih.gov/5315969/) | 1971 | N/A | Annals of Internal Medicine | Early report of PCP treated with pyrimethamine and sulfadiazine |
| [12645193](https://pubmed.ncbi.nlm.nih.gov/12645193/) | 2002 | N/A | J Formosan Med Assoc | AIDS patient with Toxoplasma brain abscess and concurrent atypical PCP treated with clindamycin plus sulfadiazine (Taiwan case) |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | Lists quinine-pyrimethamine-sulfadiazine and TMP-SMX among antiprotozoal drugs of choice, including for PCP |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Reviews therapy/prophylaxis of *Pneumocystis carinii*, *Toxoplasma gondii* and other systemic protozoan infections, including sulfadiazine regimens |
| [3914245](https://pubmed.ncbi.nlm.nih.gov/3914245/) | 1985 | N/A | Archives Françaises de Pédiatrie | Pediatric PCP in immunodeficient patients; discusses TMP-based treatment approach |
| [2011633](https://pubmed.ncbi.nlm.nih.gov/2011633/) | 1991 | Review | Primary Care | Reviews AIDS-associated parasitic diseases including PCP, noting PCP occurs in >80% of AIDS patients |
| [9097375](https://pubmed.ncbi.nlm.nih.gov/9097375/) | 1997 | Review | Seminars in Respiratory Infections | Reviews Toxoplasma pneumonia pathogenesis and treatment in immunocompromised hosts |
| [1836573](https://pubmed.ncbi.nlm.nih.gov/1836573/) | 1991 | N/A | Presse Médicale | Discusses folinic acid use to manage cytopenia from antiparasitic regimens (incl. pyrimethamine-sulfadiazine) in AIDS patients treated for PCP/toxoplasmosis |
| [1088340](https://pubmed.ncbi.nlm.nih.gov/1088340/) | 1975 | N/A | Annals of Internal Medicine | Reports hazard of folinic acid combined with pyrimethamine and sulfadiazine |

---

## Taiwan Market Information

Sulfadiazine is currently not marketed in Taiwan; no license records are available in this evidence pack (`total_licenses: 0`).

---

## Safety Considerations

TFDA label warnings and contraindications for this drug are currently a **blocking data gap** (DG001) — without this information, the candidate cannot proceed past the S1 safety screening stage. No drug-drug interaction records were found in the evidence pack either.

> Please refer to the official package insert / TFDA label for safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is currently limited to L3-level historical case series, case reports, and reviews (no clinical trials, no RCTs), and the internal scoring already places this candidate at decision stage S1 ("Research Question"). More critically, TFDA label warnings/contraindications data are missing (DG001, Blocking severity), which by definition blocks entry into safety pre-screening; the drug is also not currently marketed in Taiwan.

**To proceed, the following is needed:**
- Obtain TFDA label / package insert (warnings, contraindications) — resolves DG001, required before any safety assessment
- Obtain confirmed mechanism of action via DrugBank API — resolves DG002, needed to strengthen the mechanistic rationale
- Clarify whether prediction reflects sulfadiazine monotherapy or only sulfadiazine-pyrimethamine combination therapy for PCP
- Seek prospective or controlled clinical evidence, since current literature is limited to older case-level reports (1971–2002)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

