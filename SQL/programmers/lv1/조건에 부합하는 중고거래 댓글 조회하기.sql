/*
    USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서 
    - 2022년 10월에 작성된 
    - 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문
    - 결과는 댓글 작성일을 기준으로 오름차순 정렬
    - 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬
*/

/* KEY POINT
    1. INNER JOIN! BOARD_ID가 key임. 
*/

select b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date, '%Y-%m-%d') as created_date
from used_goods_board b
inner join used_goods_reply r on b.board_id = r.board_id 
where year(b.created_date) = 2022 and month(b.created_date) = 10
order by r.created_date asc, b.title asc