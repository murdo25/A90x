import random

#THESE ARE THE FUNCTIONS TO BE CALLED EXTERNALLY:
#workout_start()			To get the start message
#get_next_message()			To get the next workout message
#get_number_of_messages()	To get the number of times to call get_next_workout()
#workout_finish()			To get the ending message
#get_difficulty_message()	To get the question to ask about desired difficulty
#get_difficulty_response()	To get a message reporting on the chosen difficulty

class workIt:

	#workout_difficulty is 0,1, or 2  #workout_length
	def __init__(self, workout_difficulty):
		self.messages_per_exercise = 3 #including start message
		self.workout_exercises = [0,0,0,0] #only easy and medium exercises
		self.current_exercise = 0 #index of current exercise in the array
		self.exercise_timestamp = 0 #0-3, as each exercise is one minute
		self.exercises_easy = [0,1,2,3,4,5] #indecies of corresponding exercises
		self.exercises_medium = [6,7,8]
		self.exercises_hard = [9,10] #water break not included here
		self.possible_exercises = len(self.exercises_easy)+len(self.exercises_medium)+len(self.exercises_hard)

		random.seed()
		if workout_difficulty == 1:
			self.workout_exercises = [0,0,0,0,0,0,0] #only easy and medium exercises
		if workout_difficulty == 2:
			self.workout_exercises = [0,0,0,0,0,0,11,0,0,0,0]

		if workout_difficulty != 2:
			for exercise in self.workout_exercises:
				random_choice = random.randint(0,len(self.exercises_easy)+len(self.exercises_hard)-1)
				while random_choice in self.workout_exercises:
					random_choice = random.randint(0,len(self.exercises_easy)+len(self.exercises_hard)-1)
				self.workout_exercises[exercise] = random_choice
		else :
			for exercise in self.workout_exercises:
				random_choice = random.randint(0,self.possible_exercises-1)
				while random_choice in self.workout_exercises:
					random_choice = random.randint(0,self.possible_exercises-1)
				if self.workout_exercises[exercise] == 0:
					self.workout_exercises[exercise] = random_choice

#//////////////////////////////////////////////////////////////////////

	def get_next_message(self):
		message = "Error!"
		if self.current_exercise < len(self.workout_exercises):
			if self.exercise_timestamp == 0:
				if self.workout_exercises[self.current_exercise] == 0: message = self.runinplace_start()
				if self.workout_exercises[self.current_exercise] == 1: message = self.situps_start()
				if self.workout_exercises[self.current_exercise] == 2: message = self.planks_start()
				if self.workout_exercises[self.current_exercise] == 3: message = self.jumpingjacks_start()
				if self.workout_exercises[self.current_exercise] == 4: message = self.calfraises_start()
				if self.workout_exercises[self.current_exercise] == 5: message = self.wallsits_start()
				if self.workout_exercises[self.current_exercise] == 6: message = self.pushups_start()
				if self.workout_exercises[self.current_exercise] == 7: message = self.lunges_start()
				if self.workout_exercises[self.current_exercise] == 8: message = self.squats_start()
				if self.workout_exercises[self.current_exercise] == 9: message = self.suicides_start()
				if self.workout_exercises[self.current_exercise] == 10: message = self.explosions_start()
				if self.workout_exercises[self.current_exercise] == 11: message = self.waterbreak_start()
			else :
				if self.workout_exercises[self.current_exercise] == 0: message = self.runinplace_encouragement()
				if self.workout_exercises[self.current_exercise] == 1: message = self.situps_encouragement()
				if self.workout_exercises[self.current_exercise] == 2: message = self.planks_encouragement()
				if self.workout_exercises[self.current_exercise] == 3: message = self.jumpingjacks_encouragement()
				if self.workout_exercises[self.current_exercise] == 4: message = self.calfraises_encouragement()
				if self.workout_exercises[self.current_exercise] == 5: message = self.wallsits_encouragement()
				if self.workout_exercises[self.current_exercise] == 6: message = self.pushups_encouragement()
				if self.workout_exercises[self.current_exercise] == 7: message = self.lunges_encouragement()
				if self.workout_exercises[self.current_exercise] == 8: message = self.squats_encouragement()
				if self.workout_exercises[self.current_exercise] == 9: message = self.suicides_encouragement()
				if self.workout_exercises[self.current_exercise] == 10: message = self.explosions_encouragement()
				if self.workout_exercises[self.current_exercise] == 11: message = self.waterbreak_encouragement()
			if self.exercise_timestamp == self.messages_per_exercise-1 :
				self.exercise_timestamp = 0
				self.current_exercise = self.current_exercise + 1
			else : self.exercise_timestamp = self.exercise_timestamp + 1
		return message

###

	def get_number_of_messages(self):
		return len(self.workout_exercises)*4

	def get_difficulty_message(self):
		comment = ["How hard will your workout be today? Easy, medium, or hard?","What'll it be this time? Easy, medium, or hard?"]
		return comment[random.randint(0,len(comment)-1)]

	def get_difficulty_response(self):
		if workout_difficulty == 0:
			comment = ["You have chosen wimp-mode.","Commencing candy-land mode.","This will be a piece of cake!","Okay, no problem. Maybe we can do a really hard one next time.","Mode: insanely difficult. Just kidding! We'll do easy mode.","Easy mode it is!","You have chosen a warm and fuzzy workout. Doesn't it just make you feel all warm and fuzzy inside?","I knew you would say that.","That's a great place to start!","Easy it is!"]
		if workout_difficulty == 1:
			comment = ["Medocre mode, here we come.","You have selected medium. Again.","You know, I saw an eleven-year-old kid once who did eighteen-hundred situps. Who knows, maybe you can too?","Er, okay.","Difficulty: moderate.","Your audacity is like the cold of the polar ice caps. Melting.","Alright, we're working our way up!"]
		if workout_difficulty == 2:
			comment = ["Huh. Of course you would.","Are you sure you want to do that? Alright...","Huh, when pigs fly! Uh, I mean, yes! Hard mode, here we come!","Yes! You can do hard things!","You have chosen beast mode.","You have selected the horribly awful, insanely difficult master level! Otherwise known as hard.","Mission: impossible.","You. Are. Awesome."]
		return comment[random.randint(0,len(comment)-1)]

#Start/finish workout:

	def workout_start(self):
		command = ["So, you'd like to do a workout, huh. Well, let's get crackin'!","Alright, you want a workout? You're going to get a workout!","You can't possibly be serious. Well, I guess it'll mean you get more doughnuts...","A workout? A workout! You're going to work out? This'll be fun to watch!","I wish I could work out. But it's okay, you can work out for me!","A workout! I love workouts! Powerades all around!","Okay, we can do a workout... just don't knock me over when you pass out, okay?","All right, let's get ready to rumble!","Hah! You're crazy! I like that. Let's do it!"]
		return command[random.randint(0,len(command)-1)]

	def workout_finish(self):
		command = ["All right, we're done here.","That was totally wicked! Let's do that again.","Ahh, we're done already?","Okay, good work team. You can stretch and cool off now. And don't forget to drink lots of water!","OK, that's it. Woah, I feel like I've been posessed by some crazy workout genious. But don't worry! I'm back to normal, now.","Workout accomplished.","Ding! All done. And the winner is... me! Just kidding, it's you.","Great job, mate! You can stop now.","Okay, okay, that's enough for today. Better luck next time."]
		return command[random.randint(0,len(command)-1)]

#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////	
#Run in place///////////////////////////////////////////////////
#Difficulty: 1
#INDEX: 0

	def runinplace_start(self):
		command = ["Alright now, run in place! Let's move it move it move it!","Your next task is to run like the wind. Run in place! Run run run!"]
		return command[random.randint(0,len(command)-1)]
	
	def runinplace_antagonist(self):
		chaser = ["a giant man-eating gorilla!","an angry tyranosaurus rex!","a vicious, hungry, flying hammer-head shark!","an angry bull!","a horde of screeching lemurs!","a gluttonous giant 		toad!","a swarm of angry hornets!","a noxious fire-breathing dragon!","a who-knows-what from you-know-where!","a stampede of raging rhinos!","an enraged and blood-thirsty toucan!","your evil twin!","the worst thing you can think of!","your worst nightmare!","the borg.","broccoli!","a garadose!","a weeping angel.","a giant blob of green goo!"]
		return chaser[random.randint(0,len(chaser)-1)]

	def runinplace_encouragement(self):
		comment = ["Run like there's no tomorrow!","Good, you're huffing and puffing.","Run!","We cannot get out; we cannot get out. They are coming.","You're not getting anywhere; run!","Faster! You're being chased by "+self.runinplace_antagonist()+" Go go go!"]
		return comment[random.randint(0,len(comment)-1)]

#Situps/////////////////////////////////////////////////////////
#Difficulty: 1
#INDEX: 1

	def situps_start(self):
		command = ["On your back, give me a billion situps! Now, go go go!","Now, for some situps. Go! One, two, three, four, five; keep going!","Now, for another torture, uh, exercise, let's do some situps!"]
		return command[random.randint(0,len(command)-1)]

	def situps_encouragement(self):
		comment = ["Put your back into it!","Now, go faster!","Those are girl situps!","Don't you dare touch your knees!","Good job.","That's a lot of situps!","This is what you get for eating that hamburger last thursday!","Breathe in, out, in, out, in, out.","Keep going.","OK, now, faster!","Don't knock your knees together!"]
		return comment[random.randint(0,len(comment)-1)]

#Planks/////////////////////////////////////////////////////////
#Difficulty: 1
#INDEX: 2

	def planks_start(self):
		command = ["Alright, down on your elbows, back straight, core tight; it's plank time!","Now, for some planks! Get down like you're ducking all the machine-gun fire overhead; core straight, clench up those abs like you're scared to death and being shot at!","OK, let's get planking! Down on your elbows now!"]
		return command[random.randint(0,len(command)-1)]

	def planks_encouragement(self):
		comment = ["Make sure your abs are tight, and taut as a bow-string!","Have your elbows fallen off, yet? No? Then keep going!","You know, my mother used to do planks. I prefer to stand, though. She was very good at them. In fact, she was so good, the used to call her mother-board!","Don't you just love how much slower the clock goes when you're looking at it?","Wow, a minute, even thirty seconds, becomes a really really long time when you're doing planks.","What would you do if I told you there was a drone over your head?","Just keep planking, just keep planking, just keep planking planking planking.","Are you bored, yet? Get it? Ha ha, ha ha!","Do your planks, you plankety plank plank, you!"]
		return comment[random.randint(0,len(comment)-1)]

#Jumping-jacks//////////////////////////////////////////////////
#Difficulty: 1
#INDEX: 3

	def jumpingjacks_start(self):
		command = ["OK, jump for joy; it's jumping-jack time! Yay!","Time for some jumping jacks! Your favorite!","Now it's time for a rest; do some jumping jacks! You got this, these are so easy I don't know why they're in this workout regime.","Okay, get ready to do some jumping jacks!"]
		return command[random.randint(0,len(command)-1)]

	def jumpingjacks_encouragement(self):
		comment = ["To infinity, and beyond!","Stop, stop, you're doing them all wrong. Just kidding! Keep going! Up, down, up, down, up, down!","One and, two and, three and, four and, one and, two and, three and, four and!","Well, this is excited, what are you jumping for? Was there a bug on the ground?","ten-billion-and-one, ten-billion-and-two, ten-billion-and-three...","Wow, I wish I could jump like that.","Icecream wouldn't taste so good if you didn't have to work for it!"]
		return comment[random.randint(0,len(comment)-1)]

#Calf-raises////////////////////////////////////////////////////
#Difficulty: 1
#INDEX: 4

	def calfraises_start(self):
		command = ["All right, now, calf-raises, go! On your toes; up, down, up, down. Now, pick up the pace!","Next up, calf-raises! Light on your toes, now, don't toutch the ground. Here we go!"]
		return command[random.randint(0,len(command)-1)]

	def calfraises_encouragement(self):
		comment = ["You got this, these are easy! Until about number sixty-seven. Gimme ten million!","I don't wanna see those heels toutch the floor, remember!","Keep it movin' yo!","Up down up down up down up down!","Feel the burn! Isn't it wonderful!"]
		return comment[random.randint(0,len(comment)-1)]

#Wall-sits//////////////////////////////////////////////////////
#Difficulty: 1
#INDEX: 5

	def wallsits_start(self):
		command = ["Alright, quick, find a wall. We're doing wall-sits now! I'll just do a desk-sit. Get ready, start!","Let's change things up! Time for wall sits! Start as soon as you can find a wall."]
		return command[random.randint(0,len(command)-1)]

	def wallsits_encouragement(self):
		comment = ["The enrichment center promises cake after the exercise. Everyone loves cake. It's so delicious and moist.","I here-by dub thee, wall-sitter. You may not rise.","Where's your chair? Hah! You don't get one!","Wow, you must be magic.","No cheating, now. I'm watching you... always watching..."]
		return comment[random.randint(0,len(comment)-1)]

#Pushups////////////////////////////////////////////////////////
#Difficulty: 2
#INDEX: 6

	def pushups_start(self):
		command = ["OK, now, down! Gimme twenty!","And now it's pushup time! Down on the ground, and, start!","Time for pushups! Down, and, go! Go go go!"]
		return command[random.randint(0,len(command)-1)]

	def pushups_encouragement(self):
		comment = ["This is why you should eat your spinach!","This'll teach you to try to feed your vegetables to the cat, under the table!","Those are girl pushups! Back and body straight! I want you stiff and rigid as a board!","I can't hear you panting, yet!","Nose on the ground, then back up, nose on the ground, then back up! I'm watching you!","Come on, you can do better than that!","Alright, now go faster!","This is a workout, not a tanning salon! Move it your mightyness! Build those muscles!","These are pushups, not those things, whatever you're doing!","I do love pushups.","Come on, do them pushups, so you can have that doughnut!"]
		return comment[random.randint(0,len(comment)-1)]

#Lunges/////////////////////////////////////////////////////////
#Difficulty: 2
#INDEX: 7

	def lunges_start(self):
		command = ["Alrighty, now, let's roughen you up a bit! Time to start some lunges! Left... and right... and left... and right... Keep going now!","And for the next exercise, we have lunges! Oh, joy! Starting... now!"]
		return command[random.randint(0,len(command)-1)]

	def lunges_encouragement(self):
		comment = ["I can't hear your muscles screaming, yet!","Building muscles is like building a skyscraper; you have to excruciatingly shred everything that was there before and dig deep, deep down into the pain in order to build up the new! Shred! Dig! Muahahaha!","Dig deeper! Dig, deeper!","You got this, man!","Go get 'em! Turn those skinny legs into beefy sausages!","Ah, lovely, I can hear your muscles screaming in pain. It's a beautiful sound, isn't it?","I'll have you whipped, flogged, put on ze rack, and I'll have your back legs fried in butter!","Arrr, you're a pirate! Row that boat! Carry those chests of gold! You go!"]
		return comment[random.randint(0,len(comment)-1)]

#Squats/////////////////////////////////////////////////////////
#Difficulty: 2
#INDEX: 8

	def squats_start(self):
		command = ["Switch! Time for squats! Glorious squats! You're going to feel the burn on this one. Ready? Go!","Alright, squats are next! Ready, get set... go!"]
		return command[random.randint(0,len(command)-1)]

	def squats_encouragement(self):
		comment = ["Get your back straight! Vertical I say!","Your knees shouldn't extend past your toes. Work them toes!","Arms extended forward! Touch the horizon!","Up, down, up, down! Come on, let's move it, people!","Hah, you though this was fun! And then you started squats. Ooh.","There's no time like right after a workout.","Come on, let's work off all those doughnuts and twinkies!"]
		return comment[random.randint(0,len(comment)-1)]

#Suicides///////////////////////////////////////////////////////
#Difficulty: 3
#INDEX: 9

	def suicides_start(self):
		command = ["And, get ready to do some suicides! Run! Gimme some laps! Go go go!","Next up, suicides! Start running!","Are you ready to run yourself into the ground? It's time for some suicides! Let's run laps!","And now, my favorite! Suicides! Ready, set, go! Run run run!"]
		return command[random.randint(0,len(command)-1)]

	def suicides_encouragement(self):
		comment = ["Run yourself ragged!","You can do it!","My teacher always said suicides were the hardest. Just so you know.","Feel the burn! Love the pain! Ahhh!","Move it soldier, go! One two three one two three one two three one two three!","You are the mighty hunter, and you're chasing your prey! Let me hear that war cry!","Have you reached China, yet?","Oh, hey! You're not dead yet! Good, do another lap, then!","Your lungs will love you forever!","You're gonna wish you'd died! Actually these might kill you, but you can come back later, so don't worry. Then you'll go away again, then you'll come back, then go away..."]
		return comment[random.randint(0,len(comment)-1)]

#Explosions/////////////////////////////////////////////////////
#Difficulty: 3
#INDEX: 10

	def explosions_start(self):
		command = ["Switch! Next we're going to do some explosions! Quick, down on the ground, do a pushup, and on the way up pull your legs in and spring up, exploding all of you full into the air! Now, keep going! This'll be great.","And, just to spite you, we're going to do some explosions now! Quick; down, pushup, legs in, leap into into the sky, hands up! Collapse back down, and do it all again! Yay! I'm so sadistic.","And, explosions! Ready, go!"]
		return command[random.randint(0,len(command)-1)]

	def explosions_encouragement(self):
		comment = ["Ha ha, I'm so evil! Keep it up, you're doing great!","Aren't these wonderful?","Get airborn, you hopeless wingless mammal!","Let me see you get two feet off the ground! And toutch your nose to the floor when you go down! I want to see you flat! Not fat.","Aren't you just so tired right now? Well, keep going! Muahahaha!"]
		return comment[random.randint(0,len(comment)-1)]

#Water break////////////////////////////////////////////////////
#Special activity
#INDEX: 11

	def waterbreak_start(self):
		command = ["Water break! Go get a drink.","Great job! Now go take a water break before you pass out. That would be a mess.","Now, let's do a cariological hyperdermic abstraction! Just kidding, I made that up. Go take a water break."]
		return command[random.randint(0,len(command)-1)]

	def waterbreak_encouragement(self):
		comment = ["Make sure you drink lots of fluids after you finish your workout, too.","Did you know that most people are dehydrated, and they don't know it?","Did you know that you have I-don't-know-how-many gajillion miles of little water-carrying tubes in your body that need filled up?"]
		return comment[random.randint(0,len(comment)-1)]

#Stretch: Windmills/////////////////////////////////////////////
#Stretch: Trunk twists//////////////////////////////////////////
#Stretch: Reach up//////////////////////////////////////////////
#Stretch: Touch toes////////////////////////////////////////////
#Stretch: Splits////////////////////////////////////////////////
#Stretch: Star//////////////////////////////////////////////////
#Stretch: Arm-pulls/////////////////////////////////////////////
#Stretch: Breathing/////////////////////////////////////////////
