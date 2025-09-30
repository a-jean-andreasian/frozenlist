# `frozenlist`
Custom Python Data Type

It allows adding, forbids removal.

---
## Performance Breakdown

- **Set lookup**: `O(1)`
  - To be maximally precise `O(10)` worst case (but we note O(10) = O(1) since it's constant)
- **List operations**: `O(list)` (same as regular list)
- **Total**: `O(list) + O(1)` ≈ `O(list)`
