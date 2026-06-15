---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 475
evidence_level: L5
indication_count: 10
---

# Budesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Budesonide: From Asthma and Inflammatory Bowel Disease to Atopic Eczema

## One-Sentence Summary

Budesonide is a synthetic glucocorticoid clinically established for managing asthma, allergic rhinitis, and inflammatory bowel disease through potent mucosal anti-inflammatory effects.
The TxGNN model predicts it may be effective for **Atopic Eczema**,
with **2 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma, allergic rhinitis, and inflammatory bowel disease (established clinical uses; no Taiwan FDA registration on record) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Taiwan Market Status | Not marketed (0 registered licenses) |
| Number of Licenses | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Budesonide is a potent synthetic glucocorticoid that acts on glucocorticoid receptors (GR) in target tissues to suppress pro-inflammatory gene transcription. It inhibits NF-κB-mediated production of cytokines such as TNF-α, IL-6, and IL-8, and — crucially for atopic conditions — downregulates Th2-polarizing mediators including IL-4, IL-13, and IL-31. It also suppresses mast cell degranulation, reduces eosinophilic tissue infiltration, and mitigates epithelial barrier disruption. These are the exact mechanisms already leveraged in budesonide's established indications: asthma and IBD both rely on mucosal anti-inflammation as the primary therapeutic goal.

Atopic eczema shares a strikingly similar pathophysiological fingerprint. Th2-dominated immune dysregulation drives IL-4/IL-13-mediated suppression of barrier genes (including filaggrin), skin eosinophilia, and IgE sensitization — all of which fall within budesonide's mechanistic reach. A 2024 translational study (PMID 38275852) directly demonstrates this overlap by formulating budesonide-loaded polymeric nanoparticles into pH-sensitive hydrogels specifically designed for local pediatric atopic dermatitis therapy, exploiting the acidic pH shift characteristic of atopic lesions to improve targeted drug release and reduce systemic absorption.

There is, however, a clinically important counterpoint: multiple patch test studies have documented budesonide as a contact allergen specifically within the atopic dermatitis patient population (PMIDs 30053491, 24603519, 35133669, 33931866). This dual role — therapeutic agent in one context, sensitizer in another — means conventional topical budesonide formulations are not suitable as first-line treatment for atopic eczema. Novel delivery systems (e.g., nanoparticle carriers) or rigorous pre-enrollment patch testing are prerequisites for any clinical development in this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | Unknown | 150 | Severe pediatric asthma endotype study combining phenotypic, immune, metabolomic, and microbiota analyses in children aged 0–12 years; atopy and eczema are captured as comorbid background conditions, but budesonide is not the trial intervention and eczema is not a primary endpoint — indirect relevance only |
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy to prevent asthma in high-risk atopic wheezing children aged 18 months to 3 years; eczema listed among atopic risk factors at enrollment; no direct budesonide-eczema treatment arm or signal |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical/Formulation | Gels (Basel) | Budesonide-loaded Eudragit L100 nanoparticle hydrogel engineered specifically for pediatric atopic dermatitis; pH-sensitive carrier exploits atopic lesion acidity to improve local drug release and reduce systemic exposure — most directly relevant study in this dataset |
| [19875223](https://pubmed.ncbi.nlm.nih.gov/19875223/) | 2010 | RCT Subgroup | Allergologia et immunopathologia | Budesonide treatment response subgroup analysis in atopic vs. non-atopic infants/preschoolers with recurrent wheezing; suggests differential glucocorticoid responsiveness by atopic status |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Clinical Study | Pediatric Dermatology | Topical budesonide applied in 14 children (5–12 years) with atopic dermatitis over 6-week open longitudinal trial; knemometry used to assess short-term growth suppression as systemic safety signal |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Clinical Study | Dermatology (Basel) | IGF axis, bone, and collagen turnover assessed in AD children treated with topical glucocorticosteroids including budesonide; percutaneous absorption and growth-suppressive effects documented |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | RCT | J Vet Pharmacol Ther | Barazone (0.025% budesonide leave-on conditioner) placebo-controlled crossover RCT in 29 dogs with atopic dermatitis; significant reduction in CADESI skin lesion scores and pruritus scores vs. placebo |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Cross-sectional | J Am Acad Dermatol | Allergic contact dermatitis to topical medications in adult AD patients; budesonide identified among key contact sensitizers in this population — primary safety signal for this repurposing direction |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cross-sectional | Contact Dermatitis | Asian AD patients show similar or higher patch-test positivity rates vs. non-AD controls; budesonide documented as clinically relevant sensitizer in this geographic cohort |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Cross-sectional | Dermatitis | Contact hypersensitivity to the European corticosteroid series in adolescents and adults with AD; budesonide hypersensitivity confirmed in a subset — reinforces sensitization risk |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Registry Study | Contact Dermatitis | Italian SIDAPA baseline series 2018–2019: budesonide has been the European standard marker for corticosteroid hypersensitivity since 2000; declining allergy trend observed over two decades |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Intranasal corticosteroids and HPA axis suppression in allergic rhinitis with comorbid atopic dermatitis; systemic class effects of corticosteroids relevant to budesonide safety planning in atopic march patients |

---

## Taiwan Market Information

Budesonide has no products currently registered with Taiwan FDA (TFDA). Market status: not marketed in Taiwan.

No license records available for tabulation.

---

## Safety Considerations

- **Contact Sensitization Risk**: Budesonide is an established contact allergen specifically documented in atopic dermatitis patients across multiple cross-sectional and registry studies (PMIDs 30053491, 35133669, 24603519, 33931866). This represents the most critical safety concern for this repurposing direction — conventional topical budesonide may worsen or complicate atopic dermatitis in sensitized individuals. Novel delivery systems (nanoparticle encapsulation) aim to reduce this risk but require human safety validation.
- **HPA Axis Suppression**: Percutaneous absorption of topical budesonide in pediatric atopic dermatitis has been documented to produce systemic glucocorticoid effects, including measurable suppression of growth (PMID 9496795) and perturbation of IGF axis and collagen turnover (PMID 8864369). Monitoring is essential in pediatric applications.
- **Drug Interactions**: No interaction data was available from the queried sources. Refer to the package insert for full interaction profile.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Budesonide's glucocorticoid receptor mechanism directly targets the Th2-driven inflammatory core of atopic eczema, and a 2024 translational study demonstrates purpose-built nanoparticle delivery for this exact indication. However, well-documented contact sensitization risk in this patient population and an evidence base that remains at L3 — with no clinical trials directly testing budesonide against eczema as a primary endpoint — demand careful patient selection and novel formulation strategies before clinical advancement.

**To proceed, the following is needed:**
- Phase 1/2 safety and tolerability study of budesonide nanoparticle hydrogel (PMID 38275852) in human atopic dermatitis — specifically assessing sensitization rates, systemic absorption, and HPA axis impact
- Mandatory pre-enrollment patch test screening protocol to identify and exclude budesonide-sensitized patients from any future trial
- Full pharmacokinetic profiling of novel dermal delivery formats to confirm reduced systemic exposure vs. conventional topical preparations
- Retrieval of complete MOA data and contraindication profile from DrugBank API and regulatory package insert sources
- Head-to-head benchmarking design against established first-line topical corticosteroids (e.g., mometasone furoate, fluticasone propionate) with lower sensitization profiles in AD patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

