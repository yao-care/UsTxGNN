---
layout: default
title: Lovastatin
parent: Moderate Evidence (L3-L4)
nav_order: 874
evidence_level: L3
indication_count: 6
last_modified_at: 2026-10-14
description: "Lovastatin: predicted new indication Homozygous familial hypercholesterolemia (evidence level L3). Approved use: Hyperlipidemia (including familial hyperlipidemia…"
monitor_inn: "LOVASTATIN"
predicted_indications: ["homozygous familial hypercholesterolemia", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "cholesterol-ester transfer protein deficiency"]
---

# Lovastatin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **6** 
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

# Lovastatin: From Hyperlipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Lovastatin is a statin (HMG-CoA reductase inhibitor) originally used to treat hyperlipidemia and related lipid disorders.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**,
but only **1 registered clinical trial** (which does not test lovastatin) and a small set of old case-level studies support this direction. The prediction sits very close to the drug's existing indication space, so it is not a truly novel repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia (including familial hyperlipidemia, hypertriglyceridemia, atherosclerosis) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| US Market Status | Cancelled only (no currently valid licenses) |
| Number of NDAs | 3 (all cancelled; listed as ANDAs) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, lovastatin inhibits HMG-CoA reductase, the rate-limiting enzyme of cholesterol synthesis, which lowers hepatic cholesterol and upregulates LDL receptors.

Homozygous familial hypercholesterolemia (HoFH) is a severe inherited form of the same lipid problem lovastatin already treats. However, benefit depends on residual LDL receptor activity. Patients with receptor-defective mutations may respond partially, while receptor-negative patients respond poorly. One study in three receptor-negative children found no LDL-C reduction on lovastatin (PMID 3397806), whereas a single case report describes normalized cholesterol after liver transplantation plus lovastatin (PMID 3534334).

Overall, the mechanistic link is plausible but conditional. This is an extension of the existing hyperlipidemia use rather than a distinct new therapeutic area.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab (PCSK9 inhibitor) study in children and adolescents with HoFH. It does not test lovastatin and matches only the disease. |

No lovastatin-specific trial in HoFH is registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Clinical study (small) | J Pediatr | Three children with receptor-negative HoFH: lovastatin 2 mg/kg/day produced no LDL-C decrease or change in LDL turnover |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Clinical study | An Esp Pediatr | Two HoFH patients on lovastatin combined with probucol and cholestyramine; response related to LDL receptor status |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case report | JAMA | Child with HoFH after liver transplantation reached normal cholesterol with lovastatin |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | Case report | An Esp Pediatr | Receptor-defective HoFH patient treated with cholestyramine plus lovastatin |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Case report | Eur J Pediatr | 7-year-old girl with HoFH treated with LDL apheresis (HELP) with and without lovastatin |
| [2912429](https://pubmed.ncbi.nlm.nih.gov/2912429/) | 1989 | Review | Arteriosclerosis | Plasma exchange and LDL apheresis in HoFH; lovastatin plus apheresis under assessment |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review | Ann N Y Acad Sci | Pharmacologic and surgical treatment of dyslipidemic children, including lovastatin |
| [12063772](https://pubmed.ncbi.nlm.nih.gov/12063772/) | 2001 | Review | Nutr Metab Cardiovasc Dis | Rationale and timing for statins in children with FH |
| [3278832](https://pubmed.ncbi.nlm.nih.gov/3278832/) | 1988 | Review | Clin Pharm | Pharmacology and clinical profile of lovastatin as an HMG-CoA reductase inhibitor |

Several other retrieved articles concern other drugs (ezetimibe, rosuvastatin, atorvastatin) and offer no lovastatin-specific evidence.

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ANDA078296 (Lupin Pharmaceuticals) | Lovastatin | Tablet | Not available (cancelled) |
| ANDA075991 (NuCare Pharmaceuticals) | Lovastatin | Tablet | Not available (cancelled) |
| ANDA075551 (RemedyRepack) | Lovastatin | Tablet | Not available (cancelled) |

## Safety Considerations

- **Disease-level cautions (knowledge-graph data, not label text)**: Lovastatin is linked to contraindications or cautions in liver disease, gallbladder disease, myopathy and other muscle diseases, rhabdomyolysis, thrombocytopenia, diabetes and hyperglycemia, gout, blood coagulation disorders, peptic ulcer disease, acute coronary syndrome and myocardial infarction, hypotensive disorder, and hypophosphatemia, among others. These should be verified against the official label.
- **Drug Interactions**: 100 interactions were found. Notable examples:
  - **Major**: Clarithromycin
  - **Moderate**: Aprepitant, Omeprazole and other proton pump inhibitors, Metronidazole, Cimetidine, Clotrimazole, Miconazole, Simvastatin, Rosuvastatin, Troglitazone, Naltrexone, Eluxadoline, Pectin
  - **Minor**: Exenatide

Please refer to the package insert for official warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No lovastatin-specific trial exists for HoFH, and the available literature consists of small, old studies and case reports with mixed results, including no effect in receptor-negative patients. The only registered trial tests a different drug. In addition, the drug has no valid US license at present, and the package-insert safety data are missing.

**To proceed, the following is needed:**
- Official package-insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Evidence stratified by LDL receptor status (receptor-defective vs receptor-negative)
- Comparison against current HoFH standards of care (more potent statins, PCSK9 inhibitors, LDL apheresis)
- Clarification of the regulatory and commercial pathway, given the cancelled US licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

