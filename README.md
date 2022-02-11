# Parse YAML to /etc/fstab

This simple script parses YAML file into a valid `/etc/fstab` file.

## Requirements

- python 3.6+
- PyYAML

## Flow

Assuming python version mentioned in the requirements is present, you may just
install the requirements:

```
pip install -r requirements.txt
```

After that, just run the script:

```
./fstab.py
```

If `chmod +x` isn't your style, use python interpreter directly:

```
python fstab.py
```

By default `fstab.yaml` is going to be read from the CWD but you can also pass
in file as an argument:

```
./fstab.py some_other_fstab.yaml
```

## Closing Thoughts

The idea was to keep the script as simple as possible while trying to keep the
code readable. I may have overdo it a bit with `options` parsing but I believe
it's still good enough™. Initially I didn't provide handling of the file
specified as an argument but I thought it would be a nice touch so now it's
included for your convenience. Of course right afterwards it made me thinking
about `argsparse` usage, but I decided this would be too much.

I intentionally omitted `root-reserve: 10%` as it's not a setting for
`/etc/fstab` file and is instead an option for ext filesystems that can be set
using `tune2fs` (or when creating the filesystem with `mke2fs`). I would imagine
there might be some other script running against the same (set of) file(s) that
would take that value and either run `tune2fs` directly or print the command for
the administrator to execute manually.
