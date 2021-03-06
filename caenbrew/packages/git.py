from ..packaging import AutotoolsPackage, package


@package
class GitPackage(AutotoolsPackage):
    """Git is a distributed version control system with fast performance."""

    name = "git"
    homepage = "https://git-scm.com/"
    version = "2.7.4"
    artifacts = ["bin/git"]

    url = "https://www.kernel.org/pub/software/scm/git/git-2.7.4.tar.xz"
