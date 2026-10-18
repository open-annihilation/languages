# Update the packs for an engine release

Each Open Annihilation release can add interface words, and a pack that
does not translate them shows those words in English. After a release,
bring every pack up to it. The 0.8.2 update (Chinese revision 8, Ukrainian
revision 4, Korean revision 3) was made this way.

## 1. Find the new words

Build the release's `oa-tool` (or take it from a build of the release's
commit), then for each pack:

```sh
python3 tools/coverage.py zh-Hans --oa-tool /path/to/oa-tool
```

Each `missing:` line is an English text the engine has and the pack does
not translate. `not in the engine:` lines are sections the engine dropped;
remove them.

## 2. Translate them in context

For each missing text, find where the engine uses it (search the engine's
`src/` for the English) and read the code around it: which screen shows it,
what fills its places, and the texts beside it. Translate it in the pack's
own voice and terms (`docs/glossaries/<tag>.md` where there is one, and the
pack's existing words for the same things). The rules of
[adding a language](new-language.md#5-translate-the-chunks) hold: every
place and number kept, printf order kept, and never `;`, `//` or a tab in
a value.

Append the new sections at the end of the pack's `interface.tdf`, under a
comment that names what they are for:

```
// Graphics' Smooth motion.

[Smooth motion]
	{
	uk=Плавний рух;
	}
```

## 3. Raise the revision

In each changed pack's `language.yaml`, set `packaging.revision` to the
next unpublished revision and `date` to today. The published revisions are
this repository's tags (`git fetch --tags; git tag`): a pack whose latest
tag is `uk-r3` becomes revision 4. A revision that was never published may
be reused.

## 4. Check

```sh
python3 tools/check.py zh-Hans --source
python3 tools/coverage.py zh-Hans --oa-tool /path/to/oa-tool
python3 tools/build.py zh-Hans --oa-tool /path/to/oa-tool
python3 -m unittest discover -s tests
```

Then run the engine's text-fit check with the built packs, as in
[adding a language, step 9](new-language.md#9-look-at-it-in-the-game);
it takes `--check-language` once for each pack.

## 5. Commit, push and publish

Commit the packs together, naming the release and each revision:
`(feat) Translate 0.8.2's new words, as zh-Hans revision 8 and uk revision 4`.
Build the packs again from the commit, so their build information names it
and is not dirty, then publish as in
[adding a language, step 11](new-language.md#11-publish), with the
maintainer's go-ahead. Begin each pack's `notes` in its `package.toml` with
what the revision adds (`Revision 4 translates the words Open Annihilation
0.8.2 added: …`), keeping the earlier revisions' sentences after it.
