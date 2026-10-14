---
layout: default
title: Cholic Acid
parent: Moderate Evidence (L3-L4)
nav_order: 527
evidence_level: L4
indication_count: 10
---

# Cholic Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Cholic Acid: From Bile Acid Synthesis and Biliary Disorders to HIV Infectious Disease

## One-Sentence Summary

Cholic acid is a bile acid, originally used for bile acid synthesis disorders and biliary-tract-related conditions.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **0 clinical trials** and only **5 publications** (mostly in vitro or reviews), one of which suggests a possible adverse effect on viral replication.
This prediction is not supported by clinical data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bile acid synthesis disorders and biliary conditions (constipation disorder, cholelithiasis, choledocholithiasis, biliary tract disease, obstructive jaundice, cerebrotendinous xanthomatosis) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L4 |
| US Market Status | Cancelled only |
| Number of NDAs | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Pharmacology data show that cholic acid binds the bile acid receptor GPBAR1 (TGR5) and the farnesoid X receptor (FXR). It is approved by the FDA and EMA for rare bile acid synthesis disorders.

The link to HIV is weak and indirect. A 1993 in vitro study found that sodium cholate had spermicidal activity and inhibited HIV-1 reverse transcriptase, and it was tested in a vaginal sponge together with nonoxynol-9 and benzalkonium chloride. In contrast, a 2006 study found that amino-functionalized cholic acid derivatives **induced** HIV-1 replication and syncytia formation in T cells, which argues against benefit. A 2010 cohort paper only describes plasma bile acid levels in HIV patients on protease inhibitors, which is an association rather than a treatment effect.

The very high model score (99.79%) is therefore not backed by clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7688380](https://pubmed.ncbi.nlm.nih.gov/7688380/) | 1993 | Preclinical / in vitro | Hum Reprod | Sodium cholate showed spermicidal and anti-HIV-1 activity in vitro; tested in a contraceptive sponge with nonoxynol-9 and benzalkonium chloride |
| [16610808](https://pubmed.ncbi.nlm.nih.gov/16610808/) | 2006 | In vitro | J Med Chem | Amino-functionalized cholic acid derivatives induced syncytia and enhanced HIV-1 replication in T cells |
| [20030469](https://pubmed.ncbi.nlm.nih.gov/20030469/) | 2010 | Cohort / observational | Pharmacotherapy | Plasma bile acid concentrations in HIV patients on protease inhibitors, with possible relevance to hepatotoxicity |
| [7848210](https://pubmed.ncbi.nlm.nih.gov/7848210/) | 1994 | Review | Aust N Z J Obstet Gynaecol | Contraceptives and protection against STD/HIV transmission; not specific to cholic acid treatment |
| [8849197](https://pubmed.ncbi.nlm.nih.gov/8849197/) | 1995 | Review | Ann Acad Med Singapore | Barrier methods for conception and disease prevention; not specific to cholic acid treatment |

## US Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| NDA205750 (cancelled) | CHOLBAM (Mirum Pharmaceuticals Inc.) | Capsule | Not listed in the compiled data |

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver disease, gallbladder disease, diarrheal disease, cholestasis, benign recurrent intrahepatic cholestasis, familial intrahepatic cholestasis, appendicitis, sclerosing cholangitis, primary biliary cholangitis, Reynolds syndrome.
- **Drug Interactions**: 10 moderate-level interactions were identified:
  - Bile acid sequestrants (cholestyramine, colesevelam, colestipol)
  - Aluminum hydroxide and sucralfate
  - Cyclosporine
  - Phenobarbital
  - Ribociclib
  - Sorafenib
  - Tipranavir (an HIV protease inhibitor, directly relevant to the predicted indication)

  Pharmacology data also list GPBAR1 and FXR as targets.

For label-based warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone. There are no clinical trials, the only direct antiviral data are old in vitro results, and a cholic acid derivative study showed enhanced HIV-1 replication. The product's only US NDA is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data, to assess whether any plausible antiviral pathway exists
- Label-based warnings and contraindications from the FDA package insert
- Modern in vitro antiviral studies on cholic acid itself (not derivatives), including its effect on viral replication
- Review of the tipranavir interaction and other antiretroviral co-medication concerns
- If pursuing a different direction, note that the better-supported lead in the compiled predictions is **vitamin deficiency disorder** (L3), where cholic acid treats the underlying bile acid synthesis disorder. This is evidence of an indirect benefit, based on case series and retrospective cohorts rather than RCTs.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

