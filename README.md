# Mice Observer

### Before start compile cython files:

## Compilation in Windows:
```
python compile_cython.py build_ext --inplace
```

## Running in Windows:

```
python main.py --path <path to project file> --name <name to new project> --video <path to video for new project> --framerate <frame rate to run video>
```

## Compilation in Linux:
```
python3 compile_cython.py build_ext --inplace
```

## Running in Linux
```
python3 main.py --path <path to project file> --name <name to new project> --video <path to video for new project> --framerate <frame rate to run video>
```

## Creating a new project:

```
python main.py --name "C:\\repos\mice-observer\out" --video "C:\\videos\mice.mp4" --framerate 60
```

## Loading a project:
```
python main.py --path "C:\\repos\mice-observer\out"
```