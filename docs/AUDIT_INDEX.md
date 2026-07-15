# Audit index

This index lists the preserved audit stages. Original failures are intentionally retained. Corrective versions do not erase the original outputs.

| Audit | Status / verdict | Seed | Main paths |
|---|---|---:|---|
| A3 | LEGACY_SUMMARY_NO_EXPLICIT_VERDICT<br><em>legacy verified baseline</em> | — | `audits/a3_verified_summary.json` |
| A4 | LEGACY_SUMMARY_NO_EXPLICIT_VERDICT<br><em>legacy exact rate-distortion stage</em> | — | `audits/a4_exact_results/a4_summary.json` |
| A5 | loopless directed graphs; uniform induced-subset sampling<br><em>legacy projective polytope stage</em> | — | `audits/a5_exact_results/a5_summary.json` |
| A6 | loopless directed graph isomorphism classes<br><em>legacy symmetry audit</em> | — | `audits/a6_exact_results/a6_summary.json` |
| A8 | LEGACY_SUMMARY_NO_EXPLICIT_VERDICT<br><em>superseded only for the ambiguous 5,234 label by A8.1</em> | — | `audits/a8_exact_results/a8_summary.json` |
| A8.1 | PASS_FORMAL_RESOLUTION_5234_REPRESENTATIVE_CODES_6942_FULL_LABELED_PREORDERS<br><em>canonical correction for condensation-code counting</em> | — | `audits/a8_1_exact_results/a8_1_summary.json` |
| A9 | LEGACY_SUMMARY_NO_EXPLICIT_VERDICT<br><em>canonical legacy clock audit</em> | — | `audits/a9_exact_results/a9_summary.json` |
| A10 | LEGACY_SUMMARY_NO_EXPLICIT_VERDICT<br><em>canonical legacy duration audit</em> | — | `audits/a10_exact_results/a10_summary.json` |
| A11 | LEGACY_SUMMARY_NO_EXPLICIT_VERDICT<br><em>historical failed/broad classifier stage</em> | 20260712 | `audits/a11_exact_results/a11_summary.json` |
| A12 | PASS_TARGETED_2D_DISCRIMINATION<br><em>canonical targeted discrimination result</em> | 20260712 | `audits/a12_exact_results/a12_summary.json` |
| A13 | FAIL_ANALYTIC_INTERVAL_SIGNATURE<br><em>canonical failed analytic signature</em> | 20260712 | `audits/a13_exact_results/a13_summary.json` |
| A14 | PASS_COVARIANCE_AWARE_INTERVAL_SIGNATURE<br><em>canonical covariance-aware signature, later shown insufficient by A15</em> | 20260714 | `audits/a14_exact_results/a14_summary.json` |
| A15 | SYSTEMATIC_CERTIFIED_COUNTEREXAMPLES_FOUND_A14_NOT_SUFFICIENT<br><em>canonical certified counterexample result</em> | 20260715 | `audits/a15_exact_results/a15_summary.json` |
| A16 | FAIL_LOCAL_GLOBAL_COMPLEMENTARITY<br><em>canonical failed local/global complementarity protocol</em> | 20260716 | `audits/a16_exact_results/a16_summary.json` |
| A17 | FAIL_MULTISCALE_SELF_SIMILARITY<br><em>canonical failed multiscale protocol</em> | 20260718 | `audits/a17_exact_results/a17_summary.json` |
| A18 | PASS_EXACT_ORDER_MEASURE_IDENTIFIABILITY_LIMIT_ROBUST | 20260721 | `audits/a18_2_exact_results/a18_summary.json` |
| A18.1 | Files preserved; no summary JSON detected | — | `audits/a18_1_exact_results` |
| A18.2 | canonical robust order-measure identifiability version<br><em>canonical robust order-measure identifiability version</em> | — | `audits/a18_2_exact_results`<br>`audits/a18_2_order_measure_identifiability.py` |
| A19 | PASS_ENSEMBLE_COPULA_IDENTIFIABILITY_LIMIT<br><em>canonical ensemble/coupla identifiability result</em> | 20260722 | `audits/a19_exact_results/a19_summary.json` |
| A20 | PASS_MINIMAL_SYMMETRY_BREAKING_INFORMATION<br><em>canonical symmetry-breaking information audit</em> | 20260723 | `audits/a20_exact_results/a20_summary.json` |
| A21 | PASS_ENDOGENOUS_RELATIONAL_EQUIVARIANCE<br><em>canonical endogenous equivariance result</em> | 20260724 | `audits/a21_exact_results/a21_summary.json` |
| A22 | PASS_MINIMAL_PRIMITIVE_ADMISSIBILITY_AUDIT<br><em>canonical primitive admissibility audit</em> | 20260725 | `audits/a22_exact_results/a22_summary.json` |
| A23 | PASS_RZS_Q_PRIMITIVE_AND_GAUGE_AUDIT<br><em>canonical RZS q and gauge audit</em> | 20260726 | `audits/a23_exact_results/a23_summary.json` |
| A24 | PASS_Q_OPERATIONALIZATION_CRITERIA_WITH_CALIBRATION_LIMIT_CORRECTED | 20260728 | `audits/a24_1_exact_results/a24_summary.json` |
| A24.1 | canonical corrected q-operationalization audit<br><em>canonical corrected q-operationalization audit</em> | — | `audits/a24_1_exact_results`<br>`audits/a24_1_q_operational_origin_audit.py` |
| A25 | PASS_NONCIRCULAR_Q_COUPLING_WITH_LAW_UNDERDETERMINATION<br><em>canonical law-underdetermination audit</em> | 20260729 | `audits/a25_exact_results/a25_summary.json` |
| A26 | PASS_EXPONENTIAL_FAMILY_SELECTION_WITH_FREE_STRENGTH<br><em>canonical exponential-family selection result</em> | 20260730 | `audits/a26_exact_results/a26_summary.json` |
| A27 | PASS_LAMBDA_IDENTIFIABLE_BUT_NOT_DERIVED<br><em>canonical lambda-status audit</em> | 20260731 | `audits/a27_exact_results/a27_summary.json` |
| A28 | PASS_SCORE_CONTEXT_SCALE_INCOMPATIBILITY_NO_GO<br><em>canonical context-scale incompatibility no-go</em> | 20260801 | `audits/a28_exact_results/a28_summary.json` |
| A29 | FAIL_CONTEXTUAL_REFINEMENT_AUDIT<br>FAIL_CONTEXTUAL_REFINEMENT_AUDIT | 20260802<br>20260803 | `audits/a29_exact_results/a29_summary.json`<br>`audits/a29_1_exact_results/a29_summary.json` |
| A29.1 | canonical corrected protocol; verdict remains FAIL<br><em>canonical corrected protocol; verdict remains FAIL</em> | — | `audits/a29_1_contextual_refinement_audit.py`<br>`audits/a29_1_exact_results` |
| A30 | PASS_BASE_MEASURE_ORIGIN_REQUIRES_EXTRA_REFINEMENT_SEMANTICS<br><em>canonical base-measure origin audit</em> | 20260804 | `audits/a30_exact_results/a30_summary.json` |
| A31 | PASS_REFINEMENT_TREE_MEASURE_PATH_INDEPENDENT_BUT_ONTOLOGY_UNDERDETERMINED<br><em>canonical finite refinement-tree measure audit</em> | 20260805 | `audits/a31_exact_results/a31_summary.json` |
| A32 | PASS_INFINITE_PROJECTIVE_MEASURE_WITH_TERMINALITY_UNDERDETERMINED<br><em>canonical infinite projective-measure audit</em> | 20260806 | `audits/a32_exact_results/a32_summary.json` |
| A33 | PASS_PROJECTIVE_RATIO_LAW_WITH_TERMINAL_WEIGHT_UNDERDETERMINATION<br><em>canonical projective branch-fraction audit</em> | 20260807 | `audits/a33_exact_results/a33_summary.json` |
| A34 | PASS_STATIC_EFFECTIVE_SCORE_WITH_DYNAMIC_CLOSURE_OBSTRUCTION<br><em>canonical effective-score closure audit</em> | 20260808 | `audits/a34_exact_results/a34_summary.json` |
| A35 | PASS_GAUSSIAN_CLOSURE_CONDITIONAL_ON_INNOVATION_LAW<br><em>canonical conditional Gaussian-closure audit</em> | 20260808 | `audits/a35_exact_results/a35_summary.json` |
| A36 | FAIL_GAUSSIAN_NOISE_SELECTION_AUDIT | 20260809 | `audits/a36_exact_results/a36_summary.json` |
| A36.1 | PASS_CORRECTED_CLT_DIAGNOSTIC_GAUSSIAN_SELECTION_REMAINS_CONDITIONAL<br><em>canonical corrective CLT diagnostic; A36 retained as failed original</em> | 20260810 | `audits/a36_1_exact_results/a36_1_summary.json` |
| A37 | FAIL_NOISE_UNIVERSALITY_AUDIT<br>PASS_CORRECTED_PARTIAL_NOISE_UNIVERSALITY_WITH_MOMENT_AND_DEPENDENCE_LIMITS | 20260810<br>20260811 | `audits/a37_exact_results/a37_summary.json`<br>`audits/a37_1_exact_results/a37_summary.json` |
| A37.1 | canonical corrective universality result; A37 retained as failed original<br><em>canonical corrective universality result; A37 retained as failed original</em> | — | `audits/a37_1_exact_results`<br>`audits/a37_1_noise_universality_corrective.py` |
| A38 | FAIL_RZS_COARSE_GRAINING_AUDIT<br>PASS_CORRECTED_OBSERVABLE_RELATIVE_COARSE_GRAINING_WITH_OCCUPANCY_OBSTRUCTION | 20260812<br>20260813 | `audits/a38_exact_results/a38_summary.json`<br>`audits/a38_1_exact_results/a38_summary.json` |
| A38.1 | canonical corrective coarse-graining result; A38 retained as failed original<br><em>canonical corrective coarse-graining result; A38 retained as failed original</em> | — | `audits/a38_1_exact_results`<br>`audits/a38_1_rzs_coarse_graining_corrective.py` |
