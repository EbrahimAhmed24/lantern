# Evidence – Student A (EbrahimAhmed24)

## E1 – Clone Remotes

```text
origin  https://github.com/EbrahimAhmed24/lantern.git (fetch)
origin  https://github.com/EbrahimAhmed24/lantern.git (push)
```

## E2
```text
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   notes.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   notes.txt

$ git diff --cached
diff --git a/notes.txt b/notes.txt
index cb60a2d..1f668f8 100644
--- a/notes.txt
+++ b/notes.txt
@@ -1 +1 @@
-This is a draft file for the Lantern project.
\ No newline at end of file
+This is a draft file for the Lantern project.Staged change for E2

$ git diff
warning: in the working copy of 'notes.txt', LF will be replaced by CRLF the next time Git touches it
diff --git a/notes.txt b/notes.txt
index 1f668f8..341b844 100644
--- a/notes.txt
+++ b/notes.txt
@@ -1 +1,2 @@
 This is a draft file for the Lantern project.Staged change for E2
+Unstaged change for E2
```

## E4
```text
$ git log --oneline --graph --decorate -10
*   e7e2a95 (HEAD -> main) merge(tasks): combine title normalization and done flag
|\  
| * 544eb9e feat(tasks): add completion status to tasks
* | fbc93db fix(tasks): strip surrounding title whitespace
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

## E5

### Drill (a) - Amend commit message
```text
$ git commit --amend -m "docs: add version control explanation"
[main e69cac7] docs: add version control explanation
 Date: Mon Nov 2 18:53:09 2026 +0200
 1 file changed, 2 insertions(+), 1 deletion(-)

$ git reflog -2
e69cac7 HEAD@{0}: commit (amend): docs: add version control explanation
e78c85b HEAD@{1}: commit: docs: add verison control explanation
```

### Drill (c)- Recover lost commit using reflog
```text
$ git reset --hard HEAD~1
HEAD is now at 287ac63 Merge branch 'main' of [https://github.com/EbrahimAhmed24/lantern](https://github.com/EbrahimAhmed24/lantern)

$ git reflog -5
287ac63 (HEAD -> main, origin/main, origin/HEAD) HEAD@{0}: reset: moving to HEAD~1
4cd54f2 HEAD@{1}: commit: docs: add git history recovery note
287ac63 (HEAD -> main, origin/main, origin/HEAD) HEAD@{2}: pull --no-rebase origin main: Merge made by the 'ort' strategy.
e69cac7 HEAD@{3}: commit (amend): docs: add version control explanation
e78c85b HEAD@{4}: commit: docs: add verison control explanation

$ git cherry-pick 4cd54f2
[main 353b911] docs: add git history recovery note
 Date: Mon Nov 2 22:37:12 2026 +0200
 1 file changed, 2 insertions(+), 1 deletion(-)

$ git log -1 --oneline
353b911 (HEAD -> main) docs: add git history recovery note
```

## E7
```text
$ git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 16 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 334 bytes | 334.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: Review all repository rules at https://github.com/EbrahimAhmed24/lantern/rules?ref=refs%2Fheads%2Fmain
remote: 
remote: - Changes must be made through a pull request.
remote: 
To https://github.com/EbrahimAhmed24/lantern.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/EbrahimAhmed24/lantern.git'
```