### To run the DIY coverage tool:

```bash
python -m scrapy.diy_coverage.run_coverage
```

### To annotate function with branch coverage
Add `@instrument_function(X)` decorator to the function you want to annotate. `X` is the number of branches in the function.

Add `track_branch(function_name, n)` to the function you want to track. `function_name` (string) is the name of the function and `n` (int) is the branch number to track.