def solution(video_len, pos, op_start, op_end, commands):
    ms_video_len = video_len.split(':')
    cal_video_len = 60 * int(ms_video_len[0]) + int(ms_video_len[1])
    
    ms_pos = pos.split(':')
    cal_pos = 60 * int(ms_pos[0]) + int(ms_pos[1])
    
    ms_op_start = op_start.split(':')
    cal_op_start = 60 * int(ms_op_start[0]) + int(ms_op_start[1])
    
    ms_op_end = op_end.split(':')
    cal_op_end = 60 * int(ms_op_end[0]) + int(ms_op_end[1])
    
    if cal_pos >= cal_op_start and cal_pos <= cal_op_end:
        cal_pos = cal_op_end
    
    for command in commands:
        if command == 'next':
            if cal_video_len - cal_pos <= 10:
                cal_pos = cal_video_len
            else:
                cal_pos += 10
        else:
            if cal_pos <= 10:
                cal_pos = 0
            else:
                cal_pos -= 10
        if cal_pos >= cal_op_start and cal_pos <= cal_op_end:
            cal_pos = cal_op_end
    
    answer_m = cal_pos // 60
    answer_s = cal_pos % 60
    
    return f"{answer_m // 10}{answer_m % 10}:{answer_s // 10}{answer_s % 10}"
