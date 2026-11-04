# Evidence: Student B (ashraqt-1026)

## E1: Clone remotes (authentication method)

```
$ git remote -v
origin  git@github.com:EbrahimAhmed24/lantern.git (fetch)
origin  git@github.com:EbrahimAhmed24/lantern.git (push)
```

## E3: Two consecutive commits on main

```
$ git log --oneline -2
f20e1ec chore: remove temporary scratch file
096e250 chore: add temporary scratch file
```

Root tree hashes:

```
$ git rev-parse 096e250^{tree}
3fded9fc2130b906f39292f8e1d3c1bbfc4990ba
$ git rev-parse f20e1ec^{tree}
10f365f38e208f07cd0d91e3dcf9ab60dbf7a965
```

File whose stored object is identical in both commits (`storage.py`):

```
$ git rev-parse 096e250:storage.py
62c7c3f528e1319a0238177be3b858a030e0ecd6
$ git rev-parse f20e1ec:storage.py
62c7c3f528e1319a0238177be3b858a030e0ecd6
```

File whose object differs (`scratch.txt`, present in the first commit and removed in the second):

```
$ git rev-parse 096e250:scratch.txt
ded8475d57ae05fe722c48716566f0857a6de876
$ git cat-file -e f20e1ec:scratch.txt
fatal: path 'scratch.txt' does not exist in 'f20e1ec'
```

## E4: History graph after Requirement 3 merges

```
$ git log --oneline --graph --decorate -10
*   0c88e7b (HEAD -> main) merge(storage): combine JSON formatting options
|\
| * d2cbba2 (feature/pretty-json) feat(storage): format JSON output
* | 466d01a (fix/stable-key-order) fix(storage): ensure stable key ordering
|/
*   30a9a7b (origin/main, origin/HEAD) Merge branch 'main' of https://github.com/EbrahimAhmed24/lantern
|\
| * f20e1ec chore: remove temporary scratch file
| * 096e250 chore: add temporary scratch file
| * ba40084 feat(storage): add task persistence
| * cf9f9fd docs(readme): fix team table formatting
| *   01f2f55 merge(readme): integrate team contributions
| |\
| * | 096e65f docs(readme): add B to team
```

## E5: Reflog for drill (b), wrong branch

```
$ git reflog -10
d37a53a (HEAD -> main, docs/usage-heading) HEAD@{0}: merge docs/usage-heading: Fast-forward
190a764 (origin/main, origin/HEAD) HEAD@{1}: reset: moving to origin/main
d37a53a (HEAD -> main, docs/usage-heading) HEAD@{2}: checkout: moving from docs/usage-heading to main
d37a53a (HEAD -> main, docs/usage-heading) HEAD@{3}: checkout: moving from main to docs/usage-heading
d37a53a (HEAD -> main, docs/usage-heading) HEAD@{4}: commit: docs: add troubleshooting section
190a764 (origin/main, origin/HEAD) HEAD@{5}: commit (merge): Merge remote-tracking branch 'origin/main'
34ee91d HEAD@{6}: commit: chore(git): stop tracking environment secrets
f7a3bf3 HEAD@{7}: merge origin/main: Merge made by the 'ort' strategy.
a9006b0 HEAD@{8}: commit: chore(git): ignore generated and local files
2647afd HEAD@{9}: commit: chore: add generated files accidentally
```

## E6: Stash listing before it was reapplied

```
$ git stash list
stash@{0}: On feature/list-sort: wip: list --sort option
```
