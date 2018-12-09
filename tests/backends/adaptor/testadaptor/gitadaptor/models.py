from django.db import models

import pathlib
from pathlib import (
    EBADF, EINVAL, ENOENT, ENOTDIR,
    Path, PosixPath, PurePath, PurePosixPath, PureWindowsPath,
    S_ISBLK, S_ISCHR, S_ISDIR, S_ISFIFO, S_ISLNK, S_ISREG, S_ISSOCK,
    Sequence, WindowsPath)

class PathAdptr(models.Model):
    source_class = Path
    

class PythonModuleName(models.fields.Field):
    """Represents a python module name"""
    
class PythonModule(models.Model):
    """Represents an installed version of a module in memory"""
    name = PythonModuleName()
    path = PathAdptr()
    
    
    
import git

from git import (Actor, AmbiguousObjectName, BadName, BadObject, BadObjectType, BaseIndexEntry, Blob, BlobFilter, BlockingLockFile, CacheError, CheckoutError, CommandError, Commit, Diff, DiffIndex, Diffable, FetchInfo, GIT_OK, Git, GitCmdObjectDB, GitCommandError, GitCommandNotFound, GitConfigParser, GitDB, GitError, HEAD, Head, HookExecutionError, IndexEntry, IndexFile, IndexObject, InvalidDBRoot, InvalidGitRepositoryError, LockFile, NULL_TREE, NoSuchPathError, ODBError, Object, ParseError, PushInfo, RefLog, RefLogEntry, Reference, Remote, RemoteProgress, RemoteReference, Repo, RepositoryDirtyError, RootModule, RootUpdateProgress, Stats, Submodule, SymbolicReference, Tag, TagObject, TagReference, Tree, TreeModifier, UnicodeMixin, UnmergedEntriesError, UnsupportedOperation, UpdateProgress, WorkTreeRepositoryUnsupported)


#class PythonModule(:
    #__import__
    #[x for x in dir(pathlib) if x[0].isupper()]
