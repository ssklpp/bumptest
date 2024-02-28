# __version__ == '2.1.7'

from bump2version import *

current_version = get_version()
new_version = bump_version(current_version)

# 패키지 버전 정보 업데이트
set_version(new_version)

# 버전 변경 커밋 및 태그 생성
if __name__ == '__main__' :
    print(f"Bumping version from {current_version} to {new_version}")
    commit_changes()
    tag_version()