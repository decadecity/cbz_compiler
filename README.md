# CBZ compiler

Combines multiple .cbz files into one, for example compiling multiple singles into a trade.

It uses Python's zip library so only works with zip formatted archives.

Each page in the compiled archive is prefixed with the name of the source archive so, as readers sort the pages in alphabetical order, the source archives will need to be named so they form the desired order when sorted alphabetically.

## Usage

```bash
python3 cbz_compiler.py --name=Name_of_Compiled_Archive source_files/*.cbz
```

This will output all the pages contained within `source_files/*.cbz` as one archive named `Name_of_Compiled_Archive.cbz`
