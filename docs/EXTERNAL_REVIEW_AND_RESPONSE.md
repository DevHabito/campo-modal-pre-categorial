# Independent technical review and response

An independent reader manually checked several equations and independently reproduced the A3/A8 enumeration using two implementations. Five of six statistics matched exactly. The unmatched statistic was the count described as “labeled condensation-poset codes”: the reader found 6,942 under the full labeled reachability interpretation, while the manuscript reported 5,234.

A8.1 resolved the issue formally. Both numbers are correct for different encodings, but the manuscript wording was ambiguous. The full labeled count is 6,942; the original implementation's minimum-representative code count is 5,234.

The review also recommended:

- publishing code and seeds;
- distinguishing classical results, corollaries, new results, exact enumeration, Monte Carlo evidence, and regression tests;
- moving the A1–A38 laboratory chronology out of the main journal narrative;
- investigating general or asymptotic results beyond `n=5`;
- treating the current Modal Field manuscript as a formal research programme or synthesis unless stronger new theorems and a physical bridge are added.

This repository package is one response to those recommendations. The verbatim private review is not included in the public-ready repository.
