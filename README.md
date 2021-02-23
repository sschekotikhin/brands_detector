# brands_detector
Brands detector based on YOLOv5 model

## Build

```bash
make -f Makefile
```

## Test

```bash
bin/darknet detector test data/brands.data cfg/brands.cfg cfg/brands.weights -thresh 0.05
```
