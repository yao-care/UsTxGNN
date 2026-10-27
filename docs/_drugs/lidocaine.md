---
layout: default
title: Lidocaine
parent: Model Prediction Only (L5)
nav_order: 859
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lidocaine: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Neuralgia, postherpetic neuralgia, dermatitis, hemorrhoids…"
monitor_inn: "LIDOCAINE"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
---

# Lidocaine
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

## Lidocaine: From Local Anesthesia and Pain Conditions to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Lidocaine is a sodium channel–blocking local anesthetic, originally used for conditions such as neuralgia, postherpetic neuralgia, hemorrhoids, dermatitis and parasitic skin infestations.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but **no clinical trials and no publications** currently support this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neuralgia, postherpetic neuralgia, dermatitis, hemorrhoids, scabies and lice infestations, urethritis, premature ejaculation (knowledge-graph indications; no approved indication text in the US license records) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 9 records in total (1 NDA and 3 ANDAs; the rest are other marketing authorizations), all cancelled |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, lidocaine blocks voltage-gated sodium channels in sensory nerves, which is why it works as a local anesthetic and in neuropathic pain.

Punctate epithelial keratoconjunctivitis causes ocular surface irritation and pain. A sodium channel blocker could plausibly relieve these symptoms, similar to its established topical ocular anesthetic use. However, this would be symptom relief only. Lidocaine has no known disease-modifying effect on keratoconjunctivitis, and repeated use of topical anesthetics can impair corneal epithelial healing. The prediction therefore has a weak mechanistic basis beyond symptom control.

Other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Papillary conjunctivitis | 99.98% | L5 | Prediction only; any benefit would be symptomatic |
| 3 | Rosacea conjunctivitis | 99.92% | L5 | Prediction only; no anti-inflammatory or antimicrobial role |
| 4 | Exposure keratitis | 99.87% | L5 | Weak and potentially harmful; anesthetics suppress blink reflex and healing |
| 5 | Atopic conjunctivitis | 99.86% | L5 | Hypothesis-level link through sensory nerve signaling (preclinical work only) |
| 6 | Conjunctival disorder | 99.84% | L4 | Trials show use as procedural anesthesia, not disease treatment |

The remaining predictions in the top 10 (nephrotic syndrome, tinea corporis, steroid-resistant nephrotic syndrome and a non-specific "non-human animal disease" category) have no plausible therapeutic mechanism.

## Clinical Trial Evidence

Currently no related clinical trials are registered for punctate epithelial keratoconjunctivitis.

For context, the closest-ranked ocular prediction with trials is **conjunctival disorder** (rank 6). Its trials concern lidocaine as surgical anesthesia, not treatment of a disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Completed | 41 | Lidocaine gel vs subconjunctival injection for anesthesia in pterygium excision; supports ocular use and safety, but does not test disease treatment |
| [NCT01350024](https://clinicaltrials.gov/study/NCT01350024) | NA | Completed | 34 | Postoperative pain after two types of local anesthesia in drooping eyelid surgery; procedural comparison with limited relevance |

## Literature Evidence

Currently no related literature is available for punctate epithelial keratoconjunctivitis.

For context, the following publications relate to other ocular predictions. They support procedural anesthesia use or offer mechanistic context, not treatment of keratoconjunctivitis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | RCT | Eye (London) | Lidocaine 2% gel vs tetracaine 1% drops as sole topical anesthetic in primary pterygium surgery |
| [29135709](https://pubmed.ncbi.nlm.nih.gov/29135709/) | 2018 | Pilot study | Cornea | Subconjunctival injection vs 2% vs 5% lidocaine gel in pterygium surgery |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Clinical study | Acta Ophthalmol Scand | Efficacy of lidocaine 2% gel as topical anesthetic in pterygium surgery |
| [16954710](https://pubmed.ncbi.nlm.nih.gov/16954710/) | 2006 | Clinical study | Ophthalmologica | Viscous lidocaine 2% gel for pain control after pterygium surgery |
| [23330822](https://pubmed.ncbi.nlm.nih.gov/23330822/) | 2013 | Clinical study | Current Eye Research | Efficacy of different anesthetics and topical anti-inflammatory treatment for pain after intravitreal injection |
| [10696746](https://pubmed.ncbi.nlm.nih.gov/10696746/) | 2000 | Clinical study | Retina | Topical anesthesia as an alternative to peribulbar or retrobulbar anesthesia in posterior vitrectomy |
| [37819721](https://pubmed.ncbi.nlm.nih.gov/37819721/) | 2023 | Preclinical | JCI Insight | Nerve–goblet cell association promotes allergen passage in allergic conjunctivitis; suggests sensory nerves as a relevant target |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective open-label study with meta-analysis | J Neurol Neurosurg Psychiatry | Medical treatment of SUNCT/SUNA headache syndromes (neurological, not a conjunctival disease) |
| [19250287](https://pubmed.ncbi.nlm.nih.gov/19250287/) | 2009 | Review / case reports | Cephalalgia | Neuropsychiatric and cardiac side effects of lidocaine; side effects were observed in all 20 patients treated for refractory headache |
| [41995267](https://pubmed.ncbi.nlm.nih.gov/41995267/) | 2026 | Case report | Int J Risk Saf Med | Methemoglobinemia (47.6%) in a child with nephrotic syndrome using topical lidocaine, topical benzocaine and co-trimoxazole |

## US Market Information

All nine US records are cancelled; none is currently valid. No approved indication text is available in these records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA006488 | XYLOCAIN (Lidocaine HCl) | Injection, solution | Not available |
| ANDA088327 | Lidocaine Hydrochloride | Injection, solution | Not available |
| ANDA088325 | Lidocaine Hydrochloride | Injection, solution | Not available |
| ANDA209190 | Tridacaine XL | Patch | Not available |
| ANDA206463 | Lidocaine | Patch | Not available |

Four other cancelled records are topical gel or cream products (for example, Health One Pain Relief Cream with Lidocaine 4% and 5% Signature Numb cream). No ophthalmic product appears among the records compiled for this report.

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: The TxGNN knowledge graph links lidocaine to contraindication with several conditions, including hypertension, liver failure and liver disease, cirrhosis, kidney disease, epilepsy, adrenocortical insufficiency (Addison disease), hypothyroidism, open-angle glaucoma, herpes simplex virus keratitis, varicella zoster infection, atopic eczema, osteoporosis, psychotic and other mental disorders, fungal infections including dermatophytosis, potassium deficiency and gastritis. These should be verified against the official label.
- **Drug Interactions**: The interaction query returned 100 interactions. Examples of the listed ones:
  - **Major**: Bupropion
  - **Moderate**: Aprepitant, Cimetidine, liposomal morphine, Obeticholic acid, Polyethylene glycol (3350 with electrolytes), Picosulfuric acid, Sodium sulfate
  - **Minor**: Dexamethasone, Kanamycin, Neomycin, Omeprazole, Streptomycin, Troglitazone
- **Reported adverse events in the literature**: Neuropsychiatric and cardiac side effects with intravenous use in headache patients (PMID 19250287), and drug-induced methemoglobinemia with topical lidocaine combined with other methemoglobin-inducing drugs (PMID 41995267).
- **Ocular-specific concern**: Topical anesthetics can suppress the blink reflex and impair corneal epithelial healing with repeated use.

Package insert warnings were not available in the data compiled for this report. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a very high model score alone, with no clinical trials or publications for punctate epithelial keratoconjunctivitis (Evidence Level L5). Lidocaine could at most provide short-term symptom relief, it has no known effect on the underlying disease, and repeated ocular use risks impairing corneal healing. All US licenses in the compiled data are also cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking data gap for safety screening)
- Mechanism of action data for lidocaine
- Preclinical or clinical evidence that lidocaine has a benefit beyond transient pain relief in punctate epithelial keratoconjunctivitis, with attention to corneal healing
- Evaluation of the ocular formulation and route, since route compatibility has not been assessed and no ophthalmic product appears in the US records
- If an ocular surface indication is pursued, atopic conjunctivitis (rank 5) is the only prediction with a hypothesis-level mechanistic link and could be framed as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

