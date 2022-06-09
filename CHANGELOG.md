<html>
  <div class="background">
    <h1>2022/2/13</h1>
    <ul>
      <li>Added an option to change Card Info Sidebar default position</li>
      <li>Fixed description button not showing on deck overview screen</li>
      <li>Fixed a sidebar error caused by rescheduled cards</li>
    </ul>
  </div>
  <div class="background">
    <h1>2022/1/30</h1>
    <ul>
      <li>Changed load settings prompt message (forgot to do it yesterday)</li>
    </ul>
  </div>
  <div class="background">
    <h1>2022/1/29</h1>
    <ul>
      <li>Added a feature to change <font color=dodgerred>button text size</font> [go to "Button Sizes" and change button text size]</li>
      <li>Added <font color=dodgerred>another style for button intervals</font> (now you can move button intervals inside the buttons) [to change button interval style go to "Styles" tab and change button interval style]</li>
      <li>Added a feature to enable <font color=dodgerred>direct config edit</font> (serves no purpose for now, don't enable it unless you're told to | The idea is to quickly be able to add new features without having to add options in settings menu)</li>
      <li>Added an option to <font color=dodgerred>backup your settings</font> (just press Backup Settings button and it will create a backup file of your settings - you can also share your settings and button stylings with other people by sharing the settings file)</li>
      <li>Added an option to <font color=dodgerred>load settings</font> file (you can load settings and not go through settings and changing different settings and styles)</li>
      <li>Fixed button tooltip bug in python 3.10 (Thanks to <a href="https://github.com/sdvcrx">@sdvcrx</a>)</li>
      <li>Removed "Restore Defaults" button (with the new "Load Settings" function, having this extra button doesn't make sense)</li>
    </ul>
  </div>
  <div class="background">
    <h1>2021/9/22</h1>
    <ul>
      <li>Minor macOS bug fix (Hopefully -_-)</li>
    </ul>
  </div>
  <div class="background">
    <h1>2021/9/15</h1>
    <ul>
      <li>Minor bug fix</li>
    </ul>
  </div>
  <div class="background">
    <h1>2021/8/23</h1>
    <ul>
      <li>Detailed Deck Overview bug fix</li>
    </ul>
  </div>
  <div class="background">
    <h1>2021/8/22</h1>
    <ul>
      <li>Added a new method for skipping cards.<br>
        <ul>
          <li>This method is partially manual. The skipped cards won't show automatically unless you finish reviewing normal cards.</li>
          <li>This method uses Anki's "Bury" function and buries skipped cards. The skipped cards will get unburied once you exit review screen or press press <button>Show Skipped</button> Button.</li>
          <li>If you want for the skipped cards to show mid-review, you'll have to press <button>Show Skipped</button> Button or press the assigned shortcut (default shortcut is <kbd>Alt</kbd> + <kbd>C</kbd>).</li>
          <li>If you use V3 sheduler, this is the only method that'll work for you and will be chosen by default.</li>
          <li>If you use V2 scheduler you can use this method or the old method. You can choose the skip method in <code>Settings Menu -> Misc -> Skip Method</code></li>
          <li>The old method is <font color=red>Next Card</font> and the new method is <font color=red>Bury</font>.</li>
          <li>The new "Bury" method might be a bit slower, especially when you use the button. If you choose to use this method, I suggets using shortcuts for skipping cards.</li>
        </ul>
      <li>Adjusted Settings Menu height for better viewing on screens with lower resulotions</li>
      <li>Moved changelog from main Settings Menu window to a separate window</li>
    </ul>
  </div>
  <div class="background">
    <h1>2021/8/4</h1>
    <ul>
      <li>Bug fix (now ARBb is compatible with Anki 2.1.45)</li>
      <li>From now on, No update will be released for Anki versions older than 2.1.45</li>
    </ul>
  </div>
  <div class="background">
    <h1>2021/7/31</h1>
    <ul>
      <li>Bug Fix</li>
    </ul>
  </div>
  <div class="background">
    <h1>2021/7/30</h1>
    <ul>
      <li>Bug Fix</li>
    </ul>
  </div>
  <div class="background">
    <h1>2021/7/30</h1>
    <ul>
      <li>Added an option to set your custom text as button labels.<br>
      replace again, hard, good, easy, etc. text with your custom text or emoji.<br>
      To change button labels and use your own custom text, go to "Button label" tab in the settings.<br>
      To the person asking me how to change button labels -_- you can use this from now on. No need to change the code.</li>
      <li>Added an option to hide hard, good, easy buttons. (Requested)<br>
      (no I haven't forgotten to put again in the list -_- you can't hide again button).<br>
      To use this option, go to "Bottombar Buttons" and look for "Hide Buttons" part there.</li>
      <li>Added an option to change the roundness of the buttons.<br>
      To use this option, go to "Styles" tab and look for "Button Border Radius" there.</li>
      <li><font color=red>Removed</font> pressed button stats from the add-on.<br>
      For those who used it, I'll be publishing it as a separate add on named "Pressed Button Stats"</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/6/9</h1>
    <ul>
      <li>Added an option to turn off more overview stats.<br></li>
      <font color=#004182>pressed button count STILL at 90%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/12/6</h1>
    <ul>
      <li>Added another mode to overview stats (taken from "More Overview Stats 2.1")</li>
      <li>Fixed conflict with speedfocus add-on (If you use speedfocus you need to enable "Speed focus" option in ARBb settings -> Misc)</li>
    </ul>
  </div><div class="background">
    <h1>2020/6/9</h1>
    <ul>
      <li>Added an option to turn off more overview stats.<br></li>
      <font color=#004182>pressed button count STILL at 90%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/5/30</h1>
    <ul>
      <li>Changed tooltip behavior.<br>
      Now it's size won't be as size of the buttons when it's position is fixed.<br></li>
      <font color=#004182>pressed button count STILL at 90%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/5/18</h1>
    <ul>
      <li>Minor code changes/improvements.<br></li>
      <font color=#004182>pressed button count STILL at 90%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/5/15</h1>
    <ul>
      <li>Now it designs review buttons that other add-ons add (like rememorize).<br>
      it treats them like other bottombar button so their color and style<br>
      will be like other bottombar buttons</li>
      <li>you can style other bottombar buttons that are added by other add-on (like deferer button).<br>
      you'll need to change their code a bit. if you want to style them leave a comment here or on github page.<br>
      (the last picture is how the extra buttons the those add-on add look after styling them using this add-on)</li>
      <li>finally a github page :\ <a href="https://github.com/noobj2/Anki-Advanced-Review-Bottombar">Here it is</a></li>
      <li>Changed color of timer text in bottombar.<br>
      now it uses the same color you have set for other bottombar buttons text color. (not a big deal though, right?)<br></li>
      <font color=#004182>pressed button count STILL at 90%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/5/9</h1>
    <ul>
      <li>Made neon and fill designs customizable. now you can change their colors using "Colors" tab.<br>
      Enable custom colors by checking "Custom Review Button Colors" checkbox and <br>
      changing again, hard, good and easy colors.<br>
      as these designs don't have a separate hover color, changing hover colors won't<br>
      change anything about these buttons</li>
      <li>Made review bottombar buttons, deck overview buttons and main screen bottombar buttons customizable. <br>
      you can change their border and text colors in "Colors" tab by changing "General Button" text and border colors.<br>
      you can't chage text or background color for general buttons if their button style is set on default.<br>
      to change general buttons style go to "Styles" tab and change "General Buttons Style".</li>
      <li>Added an option to change show answer button border color based on card ease. <br>
      you can enable than option in "Style" tab by changing "Show Answer Border Color Style" <br>
      from "Fixed" to "Based on Card Ease". you cand change color for each ease range in "Colors" tab.<br>
      - (honestly i think it's gonna be usless for most of you :/ it was just something that i needed).</li>
      <li>+ Other settings menu and bottombar buttons changes and improvements.<br></li>
      <font color=#004182>pressed button count STILL at 90%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/28</h1>
    <ul>
      <li>Added an option to choose card type [learn, review, re-learn, cram] for button count stats</li>
      <li>Added an option to manually change decks in button count stats<br></li>
      <font color=#004182>at 90%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/5/01</h1>
    <ul>
      <li>Added total time and time per card to information shown in pressed button stats<br></li>
      <font color=#004182>at 85%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/28</h1>
    <ul>
      <li>Added an option to choose card type [learn, review, re-learn, cram] for button count stats</li>
      <li>Added an option to manually change decks in button count stats<br></li>
      <font color=#004182>at 80%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/27</h1>
    <ul>
      <li>Added an option to choose time period for button count stats</li>
      <li>Added an option to change button count stats scope</li>
      <li>Button count stats window improvements<br></li>
      <font color=#004182>at 50%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/26</h1>
    <ul>
      <li><font color=tomato>NEW FEATURE:</font> pressed button count + Percent<br>
      <font color=red>NOTE:</font> it's work in progress and very basic<br>
      the only reason i'm publishing it is that i want to hear you opinions on it and see what you need<br>
      I want to hear your ideas about it, tell me what i can do to make it better<br>
      you can Email me your ideas<br>
      however, i think some of you may want to change the time period for this option<br>
      to do that go to config -> Advanced review bottombar -> open add-on folder -> <br>
      open Button_Count.py -> go to line 47 you'll see what you need there<br>
      when you're on a deck, it shows pressed button stats for that deck, <br>
      when you're in main window, it'll show overall stats<br></li>
      <font color=#004182>at 15%<br></font>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/22</h1>
    <ul>
      <li>Made styling main screen and deck overview compatible with anki versions older than 2.1.19</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/21</h1>
    <ul>
      <li>Added an option to change main screen and deck overview buttons style<br>
      (Their style will be as other bottombar buttons style)</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/20</h1>
    <ul>
      <li>Fixed tooltip bug (where it would show hard on tooltip when you<br>
      pressed good if you were in a cutom study session )</li>
      <li> Added card info sidebar auto open (opens sidebar automatically when you review a card)</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/18</h1>
    <ul>
      <li>Minor settings menu improvements</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/17</h1>
    <ul>
      <li>Fixed Neon 1 style bug</li>
      <li>Addded correct percentage, fastest reveiw, slowest review, note ID and card ID options to card info sidebar</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/16</h1>
    <ul>
      <li>Added change button transition time option (for fill and neon designs only)</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/15</h1>
    <ul>
      <li>Added an option to change cursor type when you hover over bottombar buttons</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/14</h1>
    <ul>
      <li>Added answer tooltips</li>
      <li>Adjusted tooltips for neon and fill designs</li>
      <li>Adjusted tooltips for custom button sizes</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/13</h1>
    <ul>
      <li>Added a function to get shortcuts (Don't have to test keys that you want to set as shortcuts anymore,<br> if it's Anki's default shortcut for something, the add-on wont accept it)</li>
      <li>Moved button design tooltip to another tab (noticed it was WAY too big for lower resulotions to be useful)</li>
      <br><br><font color="red"># NOTE:</font> if you're updating from any version other than 2020/4/12 you might run into some problems trying to<br>
      open settings menu if you can't open settings menu after update open add-on folder and delete meta.json file if<br>
      that didn't help go to settings.py and put a # in front of the last line then go to tools -> add-ons and<br> press restore defaults on this addon's config page<br>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/12</h1>
    <ul>
      <li>Changed settings menu so it's easier to work with on lower resolutions (had to code it all over again)</li>
      <li>Made picking colors completely automatic (no color code copy/paste, choose the color and it's set)</li>
      <li>Added an option for you to choose settings menu's position</li>
      <li>Made wide buttons compatible with no distractions add-on</li>
      <br><br><font color="red"># NOTE:</font> After update you need to restore config to defaults in tools -> addons<br>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/8</h1>
    <ul>
      <li>settings menu bugs fixes</li>
      <li>settings menu minor adjustments for smaller screens</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/7</h1>
    <ul>
      <li>settings menu improvements</li>
      <li>added an option to color intervals</li>
      <li>added an option to style other bottombar buttons</li>
      <li>added 4 new button designs</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/6</h1>
    <ul>
      <li>minor settings menu improvements</li>
      <li>card info sidebar improvements for old scheduler</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/5</h1>
    <ul>
    <li>minor settings menu improvements</li>
    <li>added tooltips with pictures for different settings</li>
    <li>fixed card info sidebar crash bug</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/4</h1>
    <ul>
      <li>added settings menu</li>
      <li>minor settings menu adjustments</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/2</h1>
    <ul>
      <li>fix for wide buttons</li>
      <li>fixed card info sidebar problem with beta versions of anki (2.1.23 and 2.1.24)</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/4/1</h1>
    <ul>
      <li>fixed issue with limiting card reviews in card info sidebar</li>
      <li>added an option to change active button indicator from border to glow and change it's color</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/3/30</h1>
    <ul>
      <li>adjusted colors and gradients for background color change for light mode</li>
      <li>added background shadow for review buttons (enable in config)</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/3/29</h1>
    <ul>
      <li>added undo button (enable in config)</li>
      <li>fixed button color for old scheduler</li>
      <li>removed conflict with customize keyboard shortcuts add-on</li>
      <li>removed conflict with speed focus add-on (needs to be enabled in config)</li>
      <li>removed conflict with slackers add-on</li>
      <li>added an option to choose text color in review button background color change</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/3/26</h1>
    <ul>
      <li>added change button size option</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/3/25</h1>
    <ul>
      <li>added change skip and info button position option</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/3/20</h1>
    <ul>
      <li>fixed conflict with "replay button on card" add-on</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/3/7</h1>
    <ul>
      <li>adjusted the color for review buttons</li>
      <li>added an option to choose the font for the text in card info side bar in config</li>
      <li>added an option so you could limit the maximum number of previous reviews that are shown on sidebar for a card</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/3/6</h1>
    <ul>
      <li>made the info sidebar customizable, you can choose what you want to see on card info sidebar in config</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/3/4</h1>
    <ul>
      <li>fixed not showing review button colors on new in-app night mode</li>
      <li>adjusted review button text colors for new in-app night mode</li>
      <li>adjusted wide button widths</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/2/8</h1>
    <ul>
      <li>added an option for you to choose the shortcut key for skip and info buttons (in add-on config)</li>
      <li>added an option to choose the sidebar theme (in add-on config)</li>
    </ul>
  </div>
  <div class="background">
    <h1>2020/1/2</h1>
    <ul>
      <li>fix for old scheduler</li>
    </ul>
  </div>
  <div class="background">
    <h1>2019/12/14</h1>
    <ul>
      <li>Initial Release</li>
    </ul>
  </div>

</body>
</html>
