#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
import math
import json
from pathlib import Path

def main() -> int:
    p_plus = [Fraction(9,40), Fraction(7,20), Fraction(1,8), Fraction(3,10)]
    p_minus = [Fraction(11,40), Fraction(3,20), Fraction(3,8), Fraction(1,5)]
    support = [0,1,2,3]

    mean_plus = sum(Fraction(k) * p for k,p in zip(support,p_plus))
    mean_minus = sum(Fraction(k) * p for k,p in zip(support,p_minus))
    moment_plus = sum(p * Fraction(1, 2**k) for k,p in zip(support,p_plus))
    moment_minus = sum(p * Fraction(1, 2**k) for k,p in zip(support,p_minus))

    getcontext().prec = 50
    sqrt2 = Decimal(2).sqrt()
    half_plus = Decimal(23)/Decimal(80) + sqrt2/Decimal(4)
    half_minus = Decimal(37)/Decimal(80) + sqrt2/Decimal(8)
    difference = half_plus - half_minus
    exact_difference_text = "(5*sqrt(2)-7)/40"

    checks = {
        "p_plus_normalized": sum(p_plus) == 1,
        "p_minus_normalized": sum(p_minus) == 1,
        "means_equal_3_over_2": mean_plus == mean_minus == Fraction(3,2),
        "fixed_moments_equal_15_over_32": moment_plus == moment_minus == Fraction(15,32),
        "half_parameter_moments_different": difference > 0,
    }

    result = {
        "verdict": "PASS_EXACT_FOUR_POINT_NONCLOSURE_WITNESS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "mean_plus": str(mean_plus),
        "mean_minus": str(mean_minus),
        "fixed_moment_plus": str(moment_plus),
        "fixed_moment_minus": str(moment_minus),
        "half_parameter_plus": str(half_plus),
        "half_parameter_minus": str(half_minus),
        "difference_decimal": str(difference),
        "difference_exact": exact_difference_text,
    }

    out = Path(__file__).resolve().parents[1] / "manuscripts" / "foundational" / "review" / "EXACT_WITNESS_CHECK.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(result["verdict"])
    for key, value in checks.items():
        print(f"{key}: {value}")
    return 0 if all(checks.values()) else 1

if __name__ == "__main__":
    raise SystemExit(main())
