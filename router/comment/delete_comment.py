from flask import Blueprint, request, jsonify, session, url_for

from DB.DAO.comment import CommentDAO
from DB.DAO.personalKeyword import PersonalKeywordDAO
from DB.DTO.comment import Comment
from block.block import Block
from router.comment.add_comment import load_comments_from_DB
from router.filtering.filtering import filtering
from router.keyword.add_keyword import get_keywords_by_id

delete_comment_bp = Blueprint('delete_comment', __name__)

personal_keywordDB = PersonalKeywordDAO()
CommentDTO = Comment()
CommentDAO = CommentDAO()


# 입력받은 댓글 db에 업로드 후 리로드
@delete_comment_bp.route('/delete_comment', methods=['POST'])
def delete_comment():
    user_info = session['info']

    # 댓글 삭제
    CommentDAO.delete_comment(request.form['comment_index'])

    # 전체 댓글 리로드
    comments = load_comments_from_DB(url_for('news'))

    # 필터링 서비스
    if session['mode'] == 'on':
        # DB 에서 키워드 get
        keywords = get_keywords_by_id(user_info['index'])
        comments = filtering(comments, keywords)

    return jsonify(comments)

