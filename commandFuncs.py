import redditGet

# various functions for every command
global currentSubReddit
global current_subreddit_sort
# main function that works
# cd [subreddit]

default_sort = 'hot'
valid_sorts = ['hot', 'new', 'rising', 'controversial', 'top']

def cd_command(subReddit):
    global currentSubReddit
    global current_subreddit_sort


    # print 'In ' + subReddit + ' subreddit'
    print 'Displaying top subs'
    
    currentSubReddit = subReddit[1]

    if len(subReddit) > 2:

        new_sort = subReddit[2]

        # TODO: determine if user entered a sort or a dot command


        # if user entered a sort
        if new_sort in valid_sorts:
            current_subreddit_sort = new_sort
        else:
            current_subreddit_sort = default_sort

    else:
        current_subreddit_sort = default_sort
 
def cd_dot_command():
    print 'cd . command'

def cd_dot_dot_command():
    print 'cd .. command'

def ls_command():
    print 'ls command'
    print currentSubReddit
    redditGet.main_api_logic(currentSubReddit, current_subreddit_sort)

def cat_command():
    print 'cat command'

# function to print line
def print_line():
    print '--------------------------------------------------------------------------------------------------------\n'

def command_builder():
    print 'in command builder'
