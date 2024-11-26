import os
import igdb_request

def place_head(file_as_list: list):
    file_as_list.extend(['[Rainmeter]\n', 'Update=-1\n', '\n', ';neutral gray = 158, 158, 158, 255\n', '\n',
                        '[Variables]\n', 'IconSize=50\n', 'IconYPadding=75\n', ';between centre of icon to another center of icon\n', 'TextXPadding=55\n', 'TextYPadding=10\n', 'MyFontFace=Georgia\n', 'MyFontSize=18\n', 'MyFontColor= 255, 193, 7, 255\n', 'MyStringEffect=Shadow\n', '\n',
                        '[Containment]\n', 'Meter=Shape\n', 'Shape=Rectangle 0,0,#IconSize#,(#IconYPadding#*9) | Fill Color 0,0,0,5 | StrokeWidth 0\n', '\n'])

def place_games(file_as_list:list, games_list:list[:list[:str]]):
    for game_number, game in enumerate(games_list):
        # For Text Title
        file_as_list.extend([f'[{game[0]} Text]\n', 
                             'Meter=String\n', 
                             'X=#TextXPadding#\n', 
                             f'Y=(#TextYPadding#+(#IconYPadding# * {game_number}))\n', 
                             'Hidden=1\n', 
                             f'Text={game[0]}\n', 
                             'AntiAlias=1\n', 
                             'StringCase=Upper\n', 
                             'FontFace=#MyFontFace#\n', 
                             'FontSize=#MyFontSize#\n', 
                             'FontColor=#MyFontColor#\n', 
                             'StringEffect=#MyStringEffect#\n', 
                             '\n'])
        
        # For Launch Title
        file_as_list.extend([f'[{game[0]} Launch]\n', 
                             'Meter=Image\n', 
                             'X=0\n', 
                             f'Y=(#IconYPadding# * {game_number})\n', 
                             'W=#IconSize#\n', 
                             'H=#IconSize#\n', 
                             f'ImageName=#@#icons\\{game[0].lower().replace(" ", "_")}_square.png\n', 
                             f'LeftMouseUpAction=[{game[1]}]\n', 
                             f'MouseOverAction=[!ShowMeter "{game[0]} Text"][!UpdateMeter "{game[0]} Text"][!Redraw]\n', 
                             f'MouseLeaveAction=[!HideMeter "{game[0]} Text"][!UpdateMeter "{game[0]} Text"][!Redraw]\n', 
                             '\n'])
        

def check_artwork(games_list:list[:list[:str]]):
    for game_number, game in enumerate(games_list):
        if os.path.isfile(fr"C:\Users\Britant\OneDrive\Documents\Rainmeter\Skins\Maile Banako\@Resources\artworks\{game[0].lower().replace(" ", "_")}_artwork"):
            return
        else:
            # if no artwork, Download artwork
            igdb_request.download_artwork(game[0])

def main():
    file_as_list:list[:str | None] = []
    # list should be in order of display
    games_list:list[:list[:str]] = [["Genshin Impact", r'"C:\Program Files\HoYoPlay\launcher.exe"'], 
                                    ["Stardew Valley", r'"D:\Games\Stardew Valley\Stardew Valley.exe"'], 
                                    ["Valorant", r'"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live'], 
                                    ["Roblox", r'C:\Users\Britant\AppData\Local\Roblox\Versions\version-eadc3c90bb1a4267\RobloxPlayerBeta.exe'],
                                    ["Skul-The Hero Slayer", r'"D:\Games\Skul\Skul.exe"'], 
                                    ["Elden Ring", r'"D:\Games\ELDEN RING\Game\eldenring.exe"'], 
                                    ["Half Life Source", r'"D:\Games\Half-Life - Source Quadrilogy\Launch Half-Life Source.bat"'], 
                                    ["Dark Souls 2", r'"D:\Games\Dark Souls 2 - Scholar of the First Sin\language.changer.exe"'], 
                                    ["Oh My Git", r'"D:\Games\oh-my-git-windows\oh-my-git.exe"']]

    check_artwork(games_list)    

    # places all values of [Rainmeter], [Variable] and [Containment]
    # List are mutable
    place_head(file_as_list)



    place_games(file_as_list, games_list)

    # For debugging
    #print(file_as_list)

    with open(r"C:\Users\Britant\OneDrive\Documents\Rainmeter\Skins\Maile Banako\test_launcher.ini",'w') as destination_file:
        destination_file.writelines(file_as_list)



if __name__ == "__main__":
    main()