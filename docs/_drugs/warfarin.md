---
layout: default
title: Warfarin
parent: Model Prediction Only (L5)
nav_order: 1298
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
monitor_inn: "WARFARIN"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "rheumatoid arthritis", "breast fibrocystic disease", "benign mammary dysplasia"]
description: "Warfarin: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Warfarin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Warfarin: Heparin cofactor 2 deficiency
{: .text-alpha }

## One-Sentence Summary

Warfarin is an oral vitamin K antagonist anticoagulant, originally used to treat and prevent thrombotic conditions such as pulmonary embolism, thrombotic disease and intracranial embolism.
The TxGNN model predicts it may be useful for **Thrombophilia** (the highest-ranked prediction with any clinical trial), supported by **1 clinical trial** and **19 publications**.
This is largely an extension of warfarin's existing anticoagulant use rather than a truly new indication, and the evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 (conditional; see below) |
| US Market Status | Marketed (valid licenses on record: at least 4) |
| Number of NDAs | 4 (all cancelled; all are ANDA generic applications) |
| Recommended Decision | Hold |

**Note on evidence level:** The L1 grade for thrombophilia rests on a single Phase 3 trial of unknown status that tests a D-dimer-guided strategy, not warfarin alone. It does not meet the "≥2 completed Phase 3 RCTs" definition, so it should be read as conditional at best.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, warfarin is a vitamin K antagonist that reduces the synthesis of clotting factors II, VII, IX and X. Its efficacy in thrombotic disease is established, and mechanistically it may be applicable to inherited and acquired thrombophilias, in which the underlying problem is a tendency toward clot formation.

Thrombophilia is a predisposition to thrombosis, so anticoagulation for secondary prevention of venous thromboembolism is a natural fit. The same reasoning applies to the other top predictions: heparin cofactor II deficiency, factor V excess and antithrombin type 2 deficiency are all inherited prothrombotic states. These conditions overlap closely with warfarin's existing thrombotic-disease indications, so the high TxGNN scores likely reflect similarity to those indications rather than independent evidence of new benefit.

Two lower-ranked predictions look like artifacts. For **rheumatoid arthritis**, warfarin appears in four Phase 1 drug-interaction studies only as a CYP2C9 probe substrate, not as a treatment. For **breast fibrocystic disease** and **benign mammary dysplasia**, the signal appears to come from the danazol–warfarin interaction, with no therapeutic rationale.

---

## Clinical Trial Evidence

**Thrombophilia (top-ranked prediction with trial evidence)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Phase 3 | Unknown | 300 | Randomized trial testing whether D-dimer can tailor the duration of oral anticoagulation after an unprovoked deep vein thrombosis. It tests a strategy, not warfarin alone. |

**Rheumatoid arthritis (drug-interaction studies only, not efficacy)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01311622](https://clinicaltrials.gov/study/NCT01311622) | Phase 1 | Completed | 15 | Effect of fostamatinib on warfarin pharmacokinetics and anticoagulant effect |
| [NCT04246762](https://clinicaltrials.gov/study/NCT04246762) | Phase 1 | Completed | 17 | Effect of olokizumab on CYP probe substrates, including S-warfarin, in RA patients |
| [NCT01636557](https://clinicaltrials.gov/study/NCT01636557) | Phase 1 | Completed | 12 | Effect of sirukumab on CYP450 activities in RA patients, with warfarin as a probe |
| [NCT05392127](https://clinicaltrials.gov/study/NCT05392127) | Phase 1 | Completed | 24 | Effect of SHR0302 on CYP substrates, including S-warfarin, in healthy volunteers |

No clinical trials are registered for heparin cofactor 2 deficiency, factor 5 excess, antithrombin deficiency type 2, breast fibrocystic disease or benign mammary dysplasia.

---

## Literature Evidence

**Thrombophilia (selected from 19 publications)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Diagnosis and treatment of lower extremity VTE; recurrence of 20–36% within 10 years of an initial event |
| [39233011](https://pubmed.ncbi.nlm.nih.gov/39233011/) | 2024 | Review | J Thromb Haemost | ISTH communication on DOACs for secondary VTE prevention in severe thrombophilia; evidence limited to cohort and single-center studies |
| [39244017](https://pubmed.ncbi.nlm.nih.gov/39244017/) | 2024 | Review | Presse Med | Impact of thrombophilia on VTE management |
| [25387211](https://pubmed.ncbi.nlm.nih.gov/25387211/) | 2014 | Review | Postgrad Med | Diagnosis, treatment and prevention of VTE in pregnancy |
| [15706484](https://pubmed.ncbi.nlm.nih.gov/15706484/) | 2005 | Review | Semin Thromb Hemost | Management options; inherited thrombophilia should not alter anticoagulation intensity |
| [12871277](https://pubmed.ncbi.nlm.nih.gov/12871277/) | 2003 | Review | J Thromb Haemost | Management of thrombophilia and uncertainty about how test results should guide care |
| [10718793](https://pubmed.ncbi.nlm.nih.gov/10718793/) | 2000 | Not classified | Br J Surg | Warfarin-induced skin necrosis, a rare complication (0.01–0.1%) |

**Other predicted indications**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2214444](https://pubmed.ncbi.nlm.nih.gov/2214444/) | 1990 | Case report | Kyobu Geka | Right ventricular thrombosis in familial heparin cofactor II deficiency |
| [2033902](https://pubmed.ncbi.nlm.nih.gov/2033902/) | 1991 | Case report | Nihon Kyobu Shikkan Gakkai Zasshi | Congenital antithrombin deficiency with pulmonary infarction; patient had received warfarin for 7 years |
| [11570053](https://pubmed.ncbi.nlm.nih.gov/11570053/) | 2001 | Case report | J UOEH | Family with multiple thromboses; a child developed recurrent DVT despite warfarin |
| [29582922](https://pubmed.ncbi.nlm.nih.gov/29582922/) | 2017 | Case report | Hamostaseologie | Unprovoked VTE in a young patient with antithrombin type IIB deficiency |
| [16716139](https://pubmed.ncbi.nlm.nih.gov/16716139/) | 2006 | Case report/Review | Pharmacotherapy | Leflunomide raised INR in a patient on warfarin, requiring a 22% dose reduction (RA context) |
| [1591422](https://pubmed.ncbi.nlm.nih.gov/1591422/) | 1992 | Case report | Ann Pharmacother | Danazol potentiated warfarin's effect and caused bleeding (fibrocystic disease context) |

None of the literature evaluates warfarin as a treatment in a controlled setting for these predicted indications. No randomized controlled trials were identified.

---

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA040301 | Warfarin Sodium (Golden State Medical Supply) | Tablet | Not available (status: valid) |
| ANDA202202 | Warfarin Sodium (REMEDYREPACK) | Tablet | Not available (status: valid) |
| ANDA040616 | Warfarin Sodium (PD-Rx Pharmaceuticals) | Tablet | Not available (status: valid) |
| ANDA090935 | Warfarin Sodium (Golden State Medical Supply) | Tablet | Not available (status: valid) |

Warfarin is marketed in the US, and the data compiled for this report show four valid licenses. Warfarin is available only as an oral tablet.

---

## Safety Considerations

**Contraindications flagged in the knowledge graph (not label text):** Drug–disease contraindication links were found for the following conditions. They should be verified against the official package insert.
- Cardiovascular and metabolic: hypertension, congestive heart failure, hyperlipidemia (including familial), hypothyroidism/myxedema
- Liver and biliary: liver failure, liver disease, gallbladder disease, cholestasis (including benign recurrent and familial intrahepatic forms)
- Kidney: impaired renal function, nephrotic syndrome (including familial and lipoid nephrosis)
- Blood: blood coagulation disease, anemia (including macrocytic)
- Psychiatric and other: psychotic, schizophreniform, schizoaffective and other mental disorders, substance abuse/dependence, connective tissue disease, bone and cartilage disease, chronic diarrheal disease

**Drug Interactions:** The interaction screen returned 100 interacting drugs. The 20 shown include:
- **Major:** Acetylsalicylic acid (aspirin), Metronidazole
- **Moderate:** Ranitidine, Rabeprazole, Doxycycline, Hydrocortisone, Metformin, Amoxicillin, Bupropion, Aprepitant, Mesalazine, Triamcinolone, Balsalazide, Dexamethasone, Betamethasone, Budesonide, Chenodeoxycholic acid
- **Minor:** Acarbose, Albiglutide, Ascorbic acid

**Additional signals from the literature:** Warfarin-induced skin necrosis is a rare complication, and interactions with leflunomide and danazol have caused INR elevation or bleeding.

Label warnings and contraindications have not been retrieved, so please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The thrombophilia prediction largely duplicates warfarin's existing thrombotic indications, and its only trial is a Phase 3 strategy study of unknown status that does not isolate warfarin. The other inherited-deficiency predictions rest on case reports or on model output alone.
- The rheumatoid arthritis, fibrocystic breast disease and benign mammary dysplasia predictions appear to be artifacts of drug-interaction co-occurrence and have no therapeutic basis.

**To proceed, the following is needed:**
- FDA package insert warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- Confirmation of the current US marketing status, since four authorizations are listed as valid
- The final results of NCT00895505, plus comparative data for warfarin versus DOACs in severe inherited thrombophilia
- A clear definition of what would count as a new indication, given the overlap with warfarin's existing thrombotic-disease uses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

