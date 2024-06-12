
# PLEASE IGNORE - used as workspace
# final answer on coding_question_21 doc

def squares(side):
    if side == 1:
        return side*side
    return squares(side-1) + side*side

print(squares(4))

print(16 + 9 + 4+ 1)

