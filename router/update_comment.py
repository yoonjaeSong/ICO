from flask import Blueprint, request, jsonify

from DB.DAO.personalKeyword import PersonalKeywordDAO
from block import block
from block.filtering import filtering

# from app import mode
update_comment_bp = Blueprint('update_comment', __name__)

personal_keywordDB = PersonalKeywordDAO()

# 댓글 받아서 필터링 함수 호출->return값을 DB에 전달하고 웹에 전달

# 임시 db
comments = [{'userID': 'cjl', 'comment': 'test data', 'property': '+'}]
# 임시 keyword
keywords = ['sibal', 'byungsin']


def print_cm(str):
    print(str)


# 입력받은 댓글 db에 업로드 후 리로드
@update_comment_bp.route('/update_comment', methods=['POST'])
def update_comment():
    # 입력된 댓글 추출
    new_comment = {'userID': request.form['userID'], 'comment': request.form['comment'], 'property': '+'}
    # 댓글 적절성 판단
    result = block.runBlockComment(new_comment['comment'])
    new_comment['property'] = result
    comments.insert(0, new_comment)
    # db에 댓글 전송     //#comments.insert(0, new_comment)   이 과정 대신에 DB에 댓글 입력
    # insert_comment(new_comment)

    ##댓글 리로드
    # 전체 댓글 호출
    # if mode == 'ICO Service on':
    keywords = personal_keywordDB.select_keywords('abc')  # id값 주기
    # 3차 필터링 함수 호출
    labeled_comments = block.privateKeywordMatch(comments, keywords)
    filterd_comments = filtering(labeled_comments)

    return jsonify(filterd_comments)


# 적절성 유무 판단 함수


# 댓글 필터링 함수
def filtering(comments):
    for comment in comments:
        if comment['property'] == '-':
            comment['comment'] = '부적절한 댓글입니다.'
    return comments
