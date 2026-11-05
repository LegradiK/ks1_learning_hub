"""Science lessons for Science Explorers — the KS1 science programme of study.

Follows the national curriculum for England (science, key stage 1):
  Year 1: plants · animals, including humans · everyday materials · seasonal changes
  Year 2: living things and their habitats · plants · animals, including humans ·
          uses of everyday materials
  Both:   working scientifically

Lessons are grouped by topic, and each one is tagged "Year 1" or "Year 2".
To add a lesson: add one dict to LESSONS (format in app/lesson_kit.py).
"""

AREAS = {
    "scientist": {
        "name": "Be a Scientist",
        "emoji": "🥽",
        "blurb": "Ask questions, look closely and test your ideas!",
        "curriculum": "Working scientifically (Years 1 and 2)",
    },
    "plants": {
        "name": "Plants",
        "emoji": "🌱",
        "blurb": "Flowers, trees, seeds and bulbs — and what plants need to grow.",
        "curriculum": "Plants (Year 1 and Year 2)",
    },
    "animals": {
        "name": "Animals, Including Humans",
        "emoji": "🐾",
        "blurb": "Animal groups, what animals eat, your body and staying healthy.",
        "curriculum": "Animals, including humans (Year 1 and Year 2)",
    },
    "habitats": {
        "name": "Living Things and Habitats",
        "emoji": "🏞️",
        "blurb": "Alive or not? Where do animals live? Who eats who?",
        "curriculum": "Living things and their habitats (Year 2)",
    },
    "materials": {
        "name": "Materials",
        "emoji": "🧱",
        "blurb": "Wood, metal, plastic, glass — what things are made of and why.",
        "curriculum": "Everyday materials (Year 1), Uses of everyday materials (Year 2)",
    },
    "seasons": {
        "name": "Seasons and Weather",
        "emoji": "🌦️",
        "blurb": "Spring, summer, autumn and winter — and the weather they bring.",
        "curriculum": "Seasonal changes (Year 1)",
    },
}


LESSONS = [
    # ------------------------------------------------------------ working scientifically
    {
        "id": "be-a-scientist",
        "area": "scientist",
        "emoji": "🥽",
        "title": "How to Be a Scientist",
        "tag": "Year 1 & 2",
        "blurb": "Ask, look, test, sort and record — just like real scientists.",
        "pages": [
            {"emoji": "❓", "heading": "Ask a question",
             "text": "Scientists are curious. They ask questions like: Why do leaves fall? "
                     "Which ball bounces highest? What do snails eat?"},
            {"emoji": "🔍", "heading": "Look closely",
             "text": "Scientists observe — that means looking very carefully. A magnifying glass "
                     "helps you see tiny things, like the veins on a leaf."},
            {"emoji": "🧪", "heading": "Do a test",
             "text": "To find out which material keeps teddy dry, you can test them! Pour a little "
                     "water on each one and see which lets water through.",
             "fact": "A fair test only changes one thing at a time."},
            {"emoji": "🗂️", "heading": "Sort and group",
             "text": "Scientists sort things into groups — like animals with fur and animals with "
                     "feathers, or things that float and things that sink."},
            {"emoji": "📊", "heading": "Record what you find",
             "text": "Write it down, draw it, or make a tally chart or table. Then you can look "
                     "for patterns and answer your question."},
            {"emoji": "🙈", "heading": "Stay safe",
             "text": "Never look straight at the Sun — not even with sunglasses on. Wash your hands "
                     "after touching soil or animals."},
        ],
        "words": [
            ("observe", "look very carefully"),
            ("predict", "guess what will happen before you test it"),
            ("test", "try something to find out what happens"),
            ("sort", "put things into groups"),
            ("record", "write or draw what you find"),
            ("magnifying glass", "a lens that makes things look bigger"),
        ],
        "talk": "What is something you wonder about? How could you find out?",
        "quiz": [
            {"q": "What does 'observe' mean?",
             "options": ["Look very carefully", "Run very fast", "Sing a song"], "answer": 0,
             "why": "Observing means looking carefully to notice details."},
            {"q": "Which tool helps you see tiny things?",
             "options": ["A spoon", "A magnifying glass", "A ruler"], "answer": 1,
             "why": "A magnifying glass makes small things look bigger."},
            {"q": "Is it safe to look straight at the Sun with sunglasses on?",
             "options": ["Yes", "No"], "answer": 1,
             "why": "Never look straight at the Sun, even with sunglasses — it can hurt your eyes."},
            {"q": "A guess about what will happen in a test is called a…",
             "options": ["Prediction", "Picture", "Puddle"], "answer": 0,
             "why": "A prediction is what you think will happen before you test it."},
        ],
    },

    # ------------------------------------------------------------ plants
    {
        "id": "parts-of-a-plant",
        "area": "plants",
        "emoji": "🌻",
        "title": "Parts of a Plant",
        "tag": "Year 1",
        "blurb": "Roots, stem, leaves, flowers and seeds — what does each part do?",
        "pages": [
            {"emoji": "🪴", "heading": "Flowering plants",
             "text": "Most plants you see in gardens and parks are flowering plants. They have "
                     "the same main parts: roots, a stem, leaves and flowers."},
            {"emoji": "🥕", "heading": "Roots",
             "text": "Roots grow under the ground. They hold the plant in the soil and suck up "
                     "water. Carrots are roots that we eat!"},
            {"emoji": "🎋", "heading": "Stem",
             "text": "The stem holds the plant up and carries water from the roots to the leaves "
                     "and flowers, a bit like a drinking straw."},
            {"emoji": "🍃", "heading": "Leaves",
             "text": "Leaves catch sunlight. Plants use sunlight to make their own food in "
                     "their leaves."},
            {"emoji": "🌸", "heading": "Flowers and petals",
             "text": "Flowers often have bright petals. Bees and butterflies visit flowers, and "
                     "the flowers make seeds."},
            {"emoji": "🌰", "heading": "Seeds",
             "text": "Seeds can grow into new plants. Some seeds are tiny, like poppy seeds. "
                     "Some are big, like a conker or a coconut!",
             "fact": "A tree trunk is a big, strong, woody stem."},
        ],
        "words": [
            ("roots", "the part under the ground that takes in water"),
            ("stem", "holds the plant up and carries water"),
            ("leaf", "catches sunlight to make food"),
            ("petal", "the coloured part of a flower"),
            ("seed", "can grow into a new plant"),
        ],
        "talk": "Find a plant near you. Can you point to its roots, stem, leaves and flowers?",
        "quiz": [
            {"q": "Which part of a plant grows under the ground?",
             "options": ["Petals", "Roots", "Leaves"], "answer": 1,
             "why": "Roots grow under the ground and take in water."},
            {"q": "What does the stem do?",
             "options": ["Holds the plant up and carries water", "Makes noise", "Catches flies"],
             "answer": 0, "why": "The stem holds the plant up and carries water like a straw."},
            {"q": "Which part catches sunlight?",
             "options": ["The roots", "The leaves", "The seeds"], "answer": 1,
             "why": "Leaves catch sunlight so the plant can make food."},
            {"q": "A tree trunk is a big…",
             "options": ["Root", "Petal", "Stem"], "answer": 2,
             "why": "A tree trunk is a big, woody stem."},
        ],
    },
    {
        "id": "trees-and-wild-plants",
        "area": "plants",
        "emoji": "🌳",
        "title": "Trees, Wild Plants and Garden Plants",
        "tag": "Year 1",
        "blurb": "Deciduous or evergreen? Daisy or dandelion?",
        "pages": [
            {"emoji": "🍂", "heading": "Deciduous trees",
             "text": "Deciduous trees lose their leaves in autumn and grow new ones in spring. "
                     "Oak, horse chestnut, sycamore and apple trees are deciduous."},
            {"emoji": "🌲", "heading": "Evergreen trees",
             "text": "Evergreen trees keep their leaves all year round. Pine, fir, holly and "
                     "yew trees are evergreen.",
             "fact": "Christmas trees are evergreens — that's why they're still green in December!"},
            {"emoji": "🌼", "heading": "Wild plants",
             "text": "Wild plants grow by themselves, without anyone planting them. Daisies, "
                     "dandelions, buttercups, clover and nettles are wild plants."},
            {"emoji": "🌷", "heading": "Garden plants",
             "text": "Garden plants are planted by people. Sunflowers, roses, tulips and "
                     "daffodils are often grown in gardens and parks."},
            {"emoji": "⚠️", "heading": "Look, don't touch!",
             "text": "Some plants sting or prickle, like nettles and holly. Some berries are "
                     "poisonous. Never eat a plant or berry you find unless a grown-up says it's safe."},
        ],
        "words": [
            ("deciduous", "a tree that loses its leaves in autumn"),
            ("evergreen", "a tree that keeps its leaves all year"),
            ("wild plant", "a plant that grows by itself"),
            ("garden plant", "a plant that people grow on purpose"),
        ],
        "talk": "Go on a plant hunt! Which wild plants can you find near your home?",
        "quiz": [
            {"q": "A tree that loses its leaves in autumn is…",
             "options": ["Evergreen", "Deciduous"], "answer": 1,
             "why": "Deciduous trees drop their leaves in autumn."},
            {"q": "Which of these is an evergreen tree?",
             "options": ["Pine", "Oak", "Horse chestnut"], "answer": 0,
             "why": "Pine trees keep their needle-like leaves all year."},
            {"q": "Which is a wild plant?",
             "options": ["A dandelion", "A tulip in a pot", "A plastic flower"], "answer": 0,
             "why": "Dandelions grow by themselves almost everywhere!"},
            {"q": "You find some berries on a walk. What should you do?",
             "options": ["Eat them", "Don't eat them unless a grown-up says it's safe", "Throw them"],
             "answer": 1, "why": "Some berries are poisonous, so always check with a grown-up."},
        ],
    },
    {
        "id": "seeds-and-bulbs",
        "area": "plants",
        "emoji": "🌱",
        "title": "Seeds and Bulbs Grow into Plants",
        "tag": "Year 2",
        "blurb": "Watch a tiny seed turn into a big plant.",
        "pages": [
            {"emoji": "🌰", "heading": "Seeds",
             "text": "A seed has a baby plant inside it, plus a store of food. When a seed gets "
                     "water and warmth, it starts to grow. This is called germination."},
            {"emoji": "🧅", "heading": "Bulbs",
             "text": "Some plants grow from bulbs, like daffodils, tulips and onions. A bulb is "
                     "packed with stored food so the plant can start growing."},
            {"emoji": "🌱", "heading": "First shoots",
             "text": "First a root grows down into the soil. Then a shoot pushes up towards the "
                     "light, and the first leaves open."},
            {"emoji": "🌻", "heading": "Growing up",
             "text": "The plant grows taller and makes more leaves. Then it grows flowers, and "
                     "the flowers make new seeds. Then it all starts again!",
             "fact": "Seeds don't need light to start growing — they use their own stored food at first."},
            {"emoji": "📏", "heading": "Be a scientist",
             "text": "Plant a bean or sunflower seed. Measure it every few days and draw it. "
                     "How tall does it grow in a month?"},
        ],
        "words": [
            ("seed", "contains a baby plant and food"),
            ("bulb", "an underground food store that a plant grows from"),
            ("germinate", "when a seed starts to grow"),
            ("shoot", "the first green part that grows up"),
            ("mature", "fully grown"),
        ],
        "talk": "What would you like to grow? Where would you plant it?",
        "quiz": [
            {"q": "When a seed starts to grow, it…",
             "options": ["Germinates", "Melts", "Hatches"], "answer": 0,
             "why": "Germination is when a seed starts to grow."},
            {"q": "Which of these grows from a bulb?",
             "options": ["A daffodil", "An oak tree", "A sunflower"], "answer": 0,
             "why": "Daffodils grow from bulbs."},
            {"q": "What grows first from a seed?",
             "options": ["A flower", "A root", "A fruit"], "answer": 1,
             "why": "The root grows first, down into the soil."},
            {"q": "What do the flowers on a plant make?",
             "options": ["New seeds", "Rain", "Rocks"], "answer": 0,
             "why": "Flowers make seeds, which can grow into new plants."},
        ],
    },
    {
        "id": "what-plants-need",
        "area": "plants",
        "emoji": "💧",
        "title": "What Plants Need to Grow",
        "tag": "Year 2",
        "blurb": "Water, light and warmth — let's test it!",
        "pages": [
            {"emoji": "💧", "heading": "Water",
             "text": "Plants need water. Without water, their leaves droop and they wilt. "
                     "The roots take water up from the soil."},
            {"emoji": "☀️", "heading": "Light",
             "text": "Plants need light to make food in their leaves. A plant kept in a dark "
                     "cupboard turns pale and yellow, and grows thin and weak."},
            {"emoji": "🌡️", "heading": "The right temperature",
             "text": "Plants need to be not too hot and not too cold. Frost can kill many "
                     "plants, so some are kept in greenhouses in winter."},
            {"emoji": "🔬", "heading": "A fair test",
             "text": "Take two plants that are the same. Give them both water, but put one in "
                     "the light and one in a dark cupboard. Check them every day!",
             "fact": "In a fair test, only ONE thing changes — here, just the light."},
            {"emoji": "🌿", "heading": "Healthy plants",
             "text": "A healthy plant has strong stems and green leaves. Plants also take "
                     "goodness from the soil to help them grow."},
        ],
        "words": [
            ("wilt", "when a plant droops because it needs water"),
            ("light", "what plants use to make food"),
            ("temperature", "how hot or cold something is"),
            ("fair test", "a test where only one thing is changed"),
        ],
        "talk": "Do you have plants at home? How do you look after them?",
        "quiz": [
            {"q": "What happens to a plant with no water?",
             "options": ["It wilts", "It grows faster", "It turns blue"], "answer": 0,
             "why": "Without water, plants droop and wilt."},
            {"q": "A plant kept in the dark turns…",
             "options": ["Pale and yellow", "Bright red", "Shiny"], "answer": 0,
             "why": "Without light, plants can't make food and turn pale."},
            {"q": "What three things do plants need to grow well?",
             "options": ["Water, light and the right temperature", "Sweets, toys and music",
                         "Ice, wind and darkness"],
             "answer": 0, "why": "Plants need water, light and a suitable temperature."},
            {"q": "In a fair test, how many things do you change?",
             "options": ["One", "Everything"], "answer": 0,
             "why": "Only change one thing, so you know what made the difference."},
        ],
    },

    # ------------------------------------------------------------ animals including humans
    {
        "id": "animal-groups",
        "area": "animals",
        "emoji": "🦁",
        "title": "Animal Groups",
        "tag": "Year 1",
        "blurb": "Mammals, birds, fish, reptiles and amphibians.",
        "pages": [
            {"emoji": "🐕", "heading": "Mammals",
             "text": "Mammals have hair or fur. Most give birth to live babies, and the babies "
                     "drink milk from their mum. Dogs, cats, cows — and humans — are mammals!",
             "fact": "Whales and dolphins live in the sea, but they are mammals, not fish!"},
            {"emoji": "🦜", "heading": "Birds",
             "text": "Birds have feathers, wings and a beak. They lay eggs with hard shells. "
                     "Most birds can fly, but penguins and ostriches can't."},
            {"emoji": "🐟", "heading": "Fish",
             "text": "Fish live in water. They have scales and fins, and they breathe through "
                     "gills. Goldfish, salmon and sharks are fish."},
            {"emoji": "🦎", "heading": "Reptiles",
             "text": "Reptiles have dry, scaly skin. Most lay eggs on land. Snakes, lizards, "
                     "crocodiles and tortoises are reptiles."},
            {"emoji": "🐸", "heading": "Amphibians",
             "text": "Amphibians have smooth, damp skin. They lay jelly-like eggs in water. "
                     "Young amphibians live in water; adults can live on land too. Frogs, toads "
                     "and newts are amphibians."},
            {"emoji": "🐶", "heading": "Comparing animals",
             "text": "Look at a pet: does it have fur, feathers or scales? Legs, wings or fins? "
                     "Comparing body parts helps us sort animals into groups."},
        ],
        "words": [
            ("mammal", "an animal with hair or fur that feeds its babies milk"),
            ("bird", "an animal with feathers, wings and a beak"),
            ("fish", "an animal with fins and gills that lives in water"),
            ("reptile", "an animal with dry, scaly skin"),
            ("amphibian", "an animal with damp skin that starts life in water"),
        ],
        "talk": "Which animal group is your favourite animal in?",
        "quiz": [
            {"q": "Which animal group has feathers?",
             "options": ["Mammals", "Birds", "Fish"], "answer": 1,
             "why": "Only birds have feathers."},
            {"q": "A frog is an…",
             "options": ["Amphibian", "Reptile", "Insect"], "answer": 0,
             "why": "Frogs have damp skin and lay eggs in water — they are amphibians."},
            {"q": "A dolphin is a…",
             "options": ["Fish", "Mammal", "Bird"], "answer": 1,
             "why": "Dolphins breathe air and feed their babies milk, so they are mammals."},
            {"q": "Which animal is a reptile?",
             "options": ["A snake", "A rabbit", "A goldfish"], "answer": 0,
             "why": "Snakes have dry, scaly skin — they are reptiles."},
            {"q": "Humans are…",
             "options": ["Mammals", "Birds", "Reptiles"], "answer": 0,
             "why": "We have hair and babies drink milk — humans are mammals!"},
        ],
    },
    {
        "id": "what-animals-eat",
        "area": "animals",
        "emoji": "🥩",
        "title": "Carnivores, Herbivores and Omnivores",
        "tag": "Year 1",
        "blurb": "Meat-eaters, plant-eaters and animals that eat both.",
        "pages": [
            {"emoji": "🐄", "heading": "Herbivores",
             "text": "Herbivores eat only plants. Cows, rabbits, horses, sheep and giraffes are "
                     "herbivores. They often have flat teeth for chewing."},
            {"emoji": "🦁", "heading": "Carnivores",
             "text": "Carnivores eat meat — other animals. Lions, tigers, sharks, owls and "
                     "crocodiles are carnivores. They often have sharp teeth or claws."},
            {"emoji": "🐻", "heading": "Omnivores",
             "text": "Omnivores eat both plants and meat. Bears, pigs, chickens, foxes and "
                     "most humans are omnivores."},
            {"emoji": "🦷", "heading": "Clues in teeth",
             "text": "You can guess what an animal eats by looking at its teeth. Sharp, pointy "
                     "teeth tear meat. Wide, flat teeth grind plants.",
             "fact": "Pandas are bears, but they eat almost only bamboo!"},
        ],
        "words": [
            ("herbivore", "an animal that eats only plants"),
            ("carnivore", "an animal that eats meat"),
            ("omnivore", "an animal that eats plants and meat"),
            ("diet", "the food an animal usually eats"),
        ],
        "talk": "What did you eat today? Was it from plants, animals or both?",
        "quiz": [
            {"q": "An animal that eats only plants is a…",
             "options": ["Herbivore", "Carnivore", "Omnivore"], "answer": 0,
             "why": "Herbivores eat only plants."},
            {"q": "A lion is a…",
             "options": ["Herbivore", "Carnivore", "Omnivore"], "answer": 1,
             "why": "Lions eat meat, so they are carnivores."},
            {"q": "Which animal is an omnivore?",
             "options": ["A cow", "A bear", "A shark"], "answer": 1,
             "why": "Bears eat berries, roots, fish and more — both plants and meat."},
            {"q": "Sharp, pointy teeth are good for eating…",
             "options": ["Meat", "Grass"], "answer": 0,
             "why": "Sharp teeth tear meat. Flat teeth grind plants."},
        ],
    },
    {
        "id": "my-body-and-senses",
        "area": "animals",
        "emoji": "👀",
        "title": "My Body and My Senses",
        "tag": "Year 1",
        "blurb": "Name the parts of your body and your five senses.",
        "pages": [
            {"emoji": "🧍", "heading": "Parts of the body",
             "text": "Your body has a head, neck, shoulders, arms, elbows, hands, fingers, "
                     "legs, knees, feet and toes. Can you point to each one?"},
            {"emoji": "👁️", "heading": "Sight",
             "text": "You see with your eyes. They tell you about colours, shapes and how "
                     "things move."},
            {"emoji": "👂", "heading": "Hearing",
             "text": "You hear with your ears. Sounds can be loud or quiet, high or low."},
            {"emoji": "👃", "heading": "Smell",
             "text": "You smell with your nose. Smells can warn you about danger, like smoke "
                     "or food that has gone bad."},
            {"emoji": "👅", "heading": "Taste",
             "text": "You taste with your tongue. Food can taste sweet, salty, sour or bitter."},
            {"emoji": "🖐️", "heading": "Touch",
             "text": "You feel with your skin, all over your body. Things can feel rough, smooth, "
                     "hot, cold, soft or hard.",
             "fact": "Your skin is the biggest part of your body!"},
        ],
        "words": [
            ("senses", "the ways your body finds out about the world"),
            ("sight", "seeing, with your eyes"),
            ("hearing", "hearing, with your ears"),
            ("smell", "smelling, with your nose"),
            ("taste", "tasting, with your tongue"),
            ("touch", "feeling, with your skin"),
        ],
        "talk": "Close your eyes. Which senses can you still use? What can you hear and feel?",
        "quiz": [
            {"q": "How many senses do we usually talk about?",
             "options": ["Three", "Five", "Ten"], "answer": 1,
             "why": "Sight, hearing, smell, taste and touch — five senses."},
            {"q": "Which body part do you use to smell?",
             "options": ["Your nose", "Your elbow", "Your knee"], "answer": 0,
             "why": "You smell with your nose."},
            {"q": "Which sense uses your skin?",
             "options": ["Taste", "Touch", "Sight"], "answer": 1,
             "why": "Your skin feels things — that's touch."},
            {"q": "Lemons taste…",
             "options": ["Sour", "Sweet", "Salty"], "answer": 0,
             "why": "Lemons are sour — your tongue can tell!"},
        ],
    },
    {
        "id": "growing-up",
        "area": "animals",
        "emoji": "🐣",
        "title": "Animals Grow Up",
        "tag": "Year 2",
        "blurb": "Egg to chicken, frogspawn to frog, baby to adult.",
        "pages": [
            {"emoji": "👶", "heading": "Young and adults",
             "text": "All animals, including humans, have young (babies) that grow into adults. "
                     "A baby grows into a toddler, then a child, a teenager and an adult."},
            {"emoji": "🥚", "heading": "Egg to chicken",
             "text": "A hen lays an egg. A chick grows inside and hatches out. The chick grows "
                     "into an adult chicken."},
            {"emoji": "🐸", "heading": "Spawn to frog",
             "text": "A frog lays frogspawn in a pond. Tadpoles hatch out and swim. They grow "
                     "legs, lose their tails and become froglets, then adult frogs!"},
            {"emoji": "🦋", "heading": "Caterpillar to butterfly",
             "text": "A butterfly lays tiny eggs. A caterpillar hatches and eats lots of leaves. "
                     "It makes a chrysalis, and a butterfly comes out."},
            {"emoji": "🐄", "heading": "Same name or different?",
             "text": "Some young animals have special names. A young cow is a calf, a young "
                     "sheep is a lamb, a young dog is a puppy and a young cat is a kitten.",
             "fact": "A baby kangaroo is called a joey!"},
        ],
        "words": [
            ("young", "the babies of an animal"),
            ("adult", "a fully grown animal or person"),
            ("hatch", "come out of an egg"),
            ("tadpole", "a young frog that lives in water"),
            ("life cycle", "how a living thing is born, grows and has young"),
        ],
        "talk": "Look at a photo of yourself as a baby. How have you changed?",
        "quiz": [
            {"q": "A young frog is called a…",
             "options": ["Tadpole", "Chick", "Calf"], "answer": 0,
             "why": "Tadpoles hatch from frogspawn and grow into frogs."},
            {"q": "What hatches from a hen's egg?",
             "options": ["A puppy", "A chick", "A lamb"], "answer": 1,
             "why": "A chick hatches and grows into a chicken."},
            {"q": "A young sheep is called a…",
             "options": ["Kitten", "Lamb", "Joey"], "answer": 1,
             "why": "Young sheep are lambs."},
            {"q": "A caterpillar turns into a…",
             "options": ["Butterfly", "Frog", "Bird"], "answer": 0,
             "why": "After its chrysalis, a caterpillar becomes a butterfly."},
        ],
    },
    {
        "id": "staying-alive-and-healthy",
        "area": "animals",
        "emoji": "🍎",
        "title": "Staying Alive and Healthy",
        "tag": "Year 2",
        "blurb": "Water, food and air — plus exercise and keeping clean.",
        "pages": [
            {"emoji": "💧", "heading": "What all animals need",
             "text": "Every animal, including you, needs three things to stay alive: water, "
                     "food and air."},
            {"emoji": "🥦", "heading": "Eating well",
             "text": "Eat lots of different foods, with plenty of fruit and vegetables. Foods "
                     "like bread, pasta and rice give energy. Too many sweets and fizzy drinks "
                     "aren't good for your teeth."},
            {"emoji": "🚰", "heading": "Drinking water",
             "text": "Your body needs water to work properly. Drink water through the day, "
                     "especially when it's hot or you've been running around."},
            {"emoji": "⚽", "heading": "Exercise",
             "text": "Exercise makes your heart and muscles strong. Running, swimming, dancing "
                     "and playing outside all count!",
             "fact": "Your heart beats faster when you exercise — feel it after you run!"},
            {"emoji": "🧼", "heading": "Keeping clean",
             "text": "Wash your hands after the toilet and before eating, to wash away germs. "
                     "Brush your teeth twice a day and have a bath or shower."},
            {"emoji": "😴", "heading": "Sleep",
             "text": "Sleep helps your body grow and your brain rest. Children need lots of "
                     "sleep every night."},
        ],
        "words": [
            ("survive", "stay alive"),
            ("healthy", "well and strong"),
            ("exercise", "moving your body to keep it strong"),
            ("hygiene", "keeping clean to stop germs spreading"),
            ("germs", "tiny living things that can make you ill"),
        ],
        "talk": "What do you do every day to keep healthy?",
        "quiz": [
            {"q": "What do all animals need to stay alive?",
             "options": ["Water, food and air", "Toys, books and TV", "Shoes, hats and coats"],
             "answer": 0, "why": "Every animal needs water, food and air."},
            {"q": "When should you wash your hands?",
             "options": ["After the toilet and before eating", "Never", "Only on birthdays"],
             "answer": 0, "why": "Washing hands gets rid of germs."},
            {"q": "Why is exercise good for you?",
             "options": ["It makes your heart and muscles strong", "It makes you sleepy forever",
                         "It turns you green"],
             "answer": 0, "why": "Exercise keeps your heart and muscles strong."},
            {"q": "How many times a day should you brush your teeth?",
             "options": ["Twice", "Never", "Once a week"], "answer": 0,
             "why": "Brush twice a day — morning and bedtime."},
        ],
    },

    # ------------------------------------------------------------ living things & habitats
    {
        "id": "alive-dead-never-alive",
        "area": "habitats",
        "emoji": "🪨",
        "title": "Alive, Dead or Never Alive?",
        "tag": "Year 2",
        "blurb": "How can you tell if something is living?",
        "pages": [
            {"emoji": "🐛", "heading": "Living things",
             "text": "Living things move, grow, need food and water, breathe, and have young. "
                     "Animals, plants — and you — are alive!"},
            {"emoji": "🍂", "heading": "Dead",
             "text": "Some things were alive once but aren't any more. A fallen leaf, a wooden "
                     "log and a feather all came from living things."},
            {"emoji": "🪨", "heading": "Never alive",
             "text": "Some things have never been alive. Rocks, metal, plastic, glass and water "
                     "were never living."},
            {"emoji": "🔥", "heading": "Tricky ones!",
             "text": "A flame moves and grows and needs air — but it is not alive! It doesn't "
                     "eat, have young, or grow by itself the way living things do.",
             "fact": "A wooden chair was once part of a living tree, so it is 'dead', not 'never alive'."},
        ],
        "words": [
            ("living", "alive now — it grows, moves, needs food and has young"),
            ("dead", "was alive once, but isn't now"),
            ("never alive", "has never been a living thing"),
            ("life processes", "things all living things do, like growing and feeding"),
        ],
        "talk": "Look around the room. Find something living, something dead and something never alive.",
        "quiz": [
            {"q": "Which of these is alive?",
             "options": ["A rock", "A tree", "A spoon"], "answer": 1,
             "why": "A tree grows, needs water and makes seeds — it is alive."},
            {"q": "A fallen brown leaf is…",
             "options": ["Alive", "Dead", "Never alive"], "answer": 1,
             "why": "It was part of a living tree, but it isn't alive any more."},
            {"q": "A plastic bottle is…",
             "options": ["Alive", "Dead", "Never alive"], "answer": 2,
             "why": "Plastic has never been a living thing."},
            {"q": "Is fire alive?",
             "options": ["Yes", "No"], "answer": 1,
             "why": "Fire moves and grows, but it doesn't feed, breathe or have young like living things."},
        ],
    },
    {
        "id": "habitats",
        "area": "habitats",
        "emoji": "🌊",
        "title": "Habitats and Microhabitats",
        "tag": "Year 2",
        "blurb": "Every living thing has a home that suits it.",
        "pages": [
            {"emoji": "🏡", "heading": "What is a habitat?",
             "text": "A habitat is the place where a plant or animal lives. It gives them food, "
                     "water and shelter."},
            {"emoji": "🌳", "heading": "Woodland",
             "text": "Woodlands have trees for squirrels and birds to nest in, and leaves and "
                     "nuts to eat. Badgers and foxes live there too."},
            {"emoji": "🏖️", "heading": "Seashore and ocean",
             "text": "Crabs, limpets and seaweed live on the seashore. Fish, whales and octopuses "
                     "live in the ocean."},
            {"emoji": "🐒", "heading": "Rainforest and desert",
             "text": "Rainforests are hot and wet, with monkeys, parrots and frogs. Deserts are "
                     "hot and dry — camels can go a long time without drinking."},
            {"emoji": "🪵", "heading": "Microhabitats",
             "text": "A microhabitat is a very small habitat. Lift a log and you may find "
                     "woodlice, worms and beetles. They like it dark and damp!",
             "fact": "Always put the log back gently, so the minibeasts keep their home."},
            {"emoji": "🤝", "heading": "Living things need each other",
             "text": "Animals depend on plants and on each other. Birds eat seeds and insects, "
                     "and bees need flowers. Plants need bees to carry pollen."},
        ],
        "words": [
            ("habitat", "the place where an animal or plant lives"),
            ("microhabitat", "a very small habitat, like under a log"),
            ("shelter", "a safe place to hide or rest"),
            ("minibeast", "a small creature like a worm, snail or beetle"),
        ],
        "talk": "What habitats can you find near your home or school?",
        "quiz": [
            {"q": "What is a habitat?",
             "options": ["Where a living thing lives", "A kind of hat", "A type of food"],
             "answer": 0, "why": "A habitat is a living thing's home."},
            {"q": "Which animal lives in the ocean?",
             "options": ["A whale", "A squirrel", "A camel"], "answer": 0,
             "why": "Whales live in the ocean."},
            {"q": "Under a log is a good microhabitat for…",
             "options": ["Woodlice", "Elephants", "Penguins"], "answer": 0,
             "why": "Woodlice like dark, damp places like under logs."},
            {"q": "Why do woodlice live under logs?",
             "options": ["It is dark and damp", "It is sunny and dry", "It is noisy"],
             "answer": 0, "why": "Woodlice need damp, dark places to stay healthy."},
        ],
    },
    {
        "id": "food-chains",
        "area": "habitats",
        "emoji": "🐦",
        "title": "Food Chains",
        "tag": "Year 2",
        "blurb": "Who eats who? Every food chain starts with a plant.",
        "pages": [
            {"emoji": "🔗", "heading": "What is a food chain?",
             "text": "A food chain shows what eats what. The arrows mean 'is eaten by'."},
            {"emoji": "🌿", "heading": "It starts with a plant",
             "text": "Almost every food chain starts with a green plant, because plants make "
                     "their own food using sunlight."},
            {"emoji": "🐌", "heading": "A garden food chain",
             "text": "Lettuce → snail → thrush → hawk. The snail eats the lettuce, the thrush "
                     "eats the snail, and the hawk eats the thrush."},
            {"emoji": "🌊", "heading": "A sea food chain",
             "text": "Seaweed → fish → seal. Every habitat has its own food chains."},
            {"emoji": "🧑", "heading": "You are in food chains too!",
             "text": "Grass → cow → human. Wheat → human (in your bread!). Humans eat plants and animals.",
             "fact": "The animal at the top of a food chain is often a big carnivore."},
        ],
        "words": [
            ("food chain", "shows what eats what"),
            ("producer", "a plant that makes its own food"),
            ("predator", "an animal that hunts other animals"),
            ("prey", "an animal that is hunted"),
        ],
        "talk": "Make up a food chain for a fox. What does it eat? What did that eat?",
        "quiz": [
            {"q": "What does a food chain usually start with?",
             "options": ["A plant", "A lion", "A rock"], "answer": 0,
             "why": "Plants make their own food, so food chains start with them."},
            {"q": "Lettuce → snail → thrush. What eats the snail?",
             "options": ["The lettuce", "The thrush"], "answer": 1,
             "why": "The arrow points from the snail to the thrush — the thrush eats it."},
            {"q": "An animal that hunts other animals is a…",
             "options": ["Predator", "Producer", "Plant"], "answer": 0,
             "why": "Predators hunt prey."},
        ],
    },

    # ------------------------------------------------------------ materials
    {
        "id": "objects-and-materials",
        "area": "materials",
        "emoji": "🥄",
        "title": "Objects and Materials",
        "tag": "Year 1",
        "blurb": "A spoon is an object. What is it made of?",
        "pages": [
            {"emoji": "🪑", "heading": "Object or material?",
             "text": "An object is a thing, like a chair or a spoon. A material is what the "
                     "object is made from, like wood or metal."},
            {"emoji": "🪵", "heading": "Wood",
             "text": "Wood comes from trees. Tables, pencils, doors and cricket bats are often "
                     "made of wood."},
            {"emoji": "🔩", "heading": "Metal",
             "text": "Metal is strong and often shiny. Keys, coins, saucepans and paperclips are "
                     "made of metal."},
            {"emoji": "🧴", "heading": "Plastic",
             "text": "Plastic can be made into almost any shape and colour. Toys, bottles, "
                     "buckets and lunchboxes are often plastic."},
            {"emoji": "🪟", "heading": "Glass",
             "text": "Glass is hard and you can see through it, but it can break. Windows, jars "
                     "and mirrors are made of glass."},
            {"emoji": "🪨", "heading": "Rock, water and more",
             "text": "Rock, brick, paper, fabric and water are materials too. One object can be "
                     "made of different materials — a spoon can be metal, wood or plastic!"},
        ],
        "words": [
            ("object", "a thing you can see and touch"),
            ("material", "what an object is made from"),
            ("wood", "a material that comes from trees"),
            ("metal", "a strong, often shiny material"),
            ("plastic", "a material that can be made into lots of shapes"),
        ],
        "talk": "Find three objects in your kitchen. What material is each one made of?",
        "quiz": [
            {"q": "Which of these is a MATERIAL?",
             "options": ["A chair", "Wood", "A cup"], "answer": 1,
             "why": "Wood is a material. A chair and a cup are objects."},
            {"q": "A window is usually made of…",
             "options": ["Glass", "Wood", "Paper"], "answer": 0,
             "why": "Glass lets light through so we can see out."},
            {"q": "What material are keys made of?",
             "options": ["Metal", "Plastic", "Fabric"], "answer": 0,
             "why": "Keys are made of strong metal."},
            {"q": "Can the same object be made from different materials?",
             "options": ["Yes", "No"], "answer": 0,
             "why": "Spoons can be metal, wood or plastic!"},
        ],
    },
    {
        "id": "properties-of-materials",
        "area": "materials",
        "emoji": "☔",
        "title": "Properties of Materials",
        "tag": "Year 1",
        "blurb": "Hard or soft? Shiny or dull? Waterproof or absorbent?",
        "pages": [
            {"emoji": "🧱", "heading": "Hard and soft",
             "text": "A property tells you what a material is like. Rock and metal are hard. "
                     "Cotton wool and wool are soft."},
            {"emoji": "✨", "heading": "Shiny and dull",
             "text": "Shiny materials reflect light, like foil and polished metal. Dull materials "
                     "don't shine, like wood and cardboard."},
            {"emoji": "🎈", "heading": "Stretchy and stiff",
             "text": "Elastic bands and balloons are stretchy. A wooden ruler is stiff — it "
                     "doesn't stretch."},
            {"emoji": "☔", "heading": "Waterproof and absorbent",
             "text": "Waterproof materials don't let water through, like plastic and rubber. "
                     "Absorbent materials soak up water, like sponges, towels and kitchen roll."},
            {"emoji": "🪟", "heading": "See-through or not",
             "text": "Transparent materials let you see through them, like clear glass. Opaque "
                     "materials don't, like wood and brick.",
             "fact": "A good umbrella must be waterproof — test materials to find the best one!"},
        ],
        "words": [
            ("property", "what a material is like"),
            ("waterproof", "doesn't let water through"),
            ("absorbent", "soaks up water"),
            ("transparent", "you can see through it"),
            ("opaque", "you can't see through it"),
            ("flexible", "bends easily"),
        ],
        "talk": "What material would be best for a dog's bed? Why?",
        "quiz": [
            {"q": "Which material is absorbent?",
             "options": ["A sponge", "A metal spoon", "A glass jar"], "answer": 0,
             "why": "Sponges soak up water — they are absorbent."},
            {"q": "Which material would make the best umbrella?",
             "options": ["Paper", "Waterproof plastic", "Kitchen roll"], "answer": 1,
             "why": "An umbrella needs a waterproof material."},
            {"q": "A material you can see through is…",
             "options": ["Transparent", "Opaque"], "answer": 0,
             "why": "Transparent means see-through."},
            {"q": "Which is stretchy?",
             "options": ["An elastic band", "A brick", "A wooden ruler"], "answer": 0,
             "why": "Elastic bands stretch and go back to their shape."},
        ],
    },
    {
        "id": "choosing-materials",
        "area": "materials",
        "emoji": "🏗️",
        "title": "Choosing the Right Material",
        "tag": "Year 2",
        "blurb": "Why are windows glass and not wood?",
        "pages": [
            {"emoji": "🤔", "heading": "Is it suitable?",
             "text": "A material is suitable if it is good for the job. Engineers think about a "
                     "material's properties before they choose it."},
            {"emoji": "🏠", "heading": "Building a house",
             "text": "Bricks and rock are strong and hard for walls. Glass is transparent for "
                     "windows. Wood is strong but light enough for doors."},
            {"emoji": "🥄", "heading": "One job, many materials",
             "text": "Spoons can be metal, plastic or wood. They all work because they are "
                     "strong enough and safe to eat with."},
            {"emoji": "🪙", "heading": "One material, many jobs",
             "text": "Metal makes coins, cars, cans and saucepans. Paper and cardboard make books, "
                     "boxes and envelopes."},
            {"emoji": "🧥", "heading": "Inventors of materials",
             "text": "Charles Macintosh invented a waterproof fabric for raincoats. John Dunlop "
                     "made air-filled rubber tyres. John McAdam invented a better way to make roads.",
             "fact": "Some people still call a raincoat a 'mac' after Charles Macintosh!"},
            {"emoji": "🐷", "heading": "In stories",
             "text": "In The Three Little Pigs, the straw and stick houses fell down, but the "
                     "brick house was strong. Brick was the most suitable material!"},
        ],
        "words": [
            ("suitable", "good for the job"),
            ("property", "what a material is like"),
            ("strong", "doesn't break easily"),
            ("inventor", "someone who makes something new"),
        ],
        "talk": "Would a chocolate teapot work? Why not?",
        "quiz": [
            {"q": "Why are windows made of glass?",
             "options": ["It is transparent", "It is soft", "It is stretchy"], "answer": 0,
             "why": "Glass is transparent, so light comes in and we can see out."},
            {"q": "Which house stayed standing in The Three Little Pigs?",
             "options": ["Straw", "Sticks", "Brick"], "answer": 2,
             "why": "Brick is strong and hard, so it was the most suitable."},
            {"q": "Who invented a waterproof fabric for raincoats?",
             "options": ["Charles Macintosh", "John Dunlop", "Neil Armstrong"], "answer": 0,
             "why": "Charles Macintosh — that's why raincoats are called macs."},
            {"q": "Which material is NOT suitable for a teapot?",
             "options": ["Chocolate", "Metal", "Pottery"], "answer": 0,
             "why": "Chocolate would melt in hot tea!"},
        ],
    },
    {
        "id": "changing-shape",
        "area": "materials",
        "emoji": "🧽",
        "title": "Squash, Bend, Twist and Stretch",
        "tag": "Year 2",
        "blurb": "Which materials can change shape?",
        "pages": [
            {"emoji": "🤏", "heading": "Squashing",
             "text": "Some objects can be squashed. A sponge or a ball of dough squashes when "
                     "you press it. A stone won't squash."},
            {"emoji": "🥢", "heading": "Bending",
             "text": "A pipe cleaner and a plastic straw can bend. A dry stick might snap "
                     "instead!"},
            {"emoji": "🌀", "heading": "Twisting",
             "text": "You can twist a pipe cleaner, a sweet wrapper or a wet cloth when you "
                     "wring it out."},
            {"emoji": "🎈", "heading": "Stretching",
             "text": "Elastic bands, balloons and some fabrics can stretch. Elastic goes back to "
                     "its shape when you let go."},
            {"emoji": "🔬", "heading": "Test it!",
             "text": "Collect objects made of different materials. Try to squash, bend, twist and "
                     "stretch each one. Record what happens in a table.",
             "fact": "Play dough stays in its new shape. A sponge springs back!"},
        ],
        "words": [
            ("squash", "press something so it gets flatter"),
            ("bend", "make something curve"),
            ("twist", "turn the ends in different directions"),
            ("stretch", "pull something so it gets longer"),
        ],
        "talk": "Which toys at home can you squash, bend, twist or stretch?",
        "quiz": [
            {"q": "Which object can you stretch?",
             "options": ["An elastic band", "A brick", "A glass"], "answer": 0,
             "why": "Elastic bands stretch and spring back."},
            {"q": "What happens if you squash a sponge and let go?",
             "options": ["It springs back", "It disappears", "It turns to water"], "answer": 0,
             "why": "Sponges spring back to their shape."},
            {"q": "Which can you bend without breaking?",
             "options": ["A pipe cleaner", "A glass jar", "A stone"], "answer": 0,
             "why": "Pipe cleaners are bendy and flexible."},
        ],
    },

    # ------------------------------------------------------------ seasons
    {
        "id": "four-seasons",
        "area": "seasons",
        "emoji": "🍁",
        "title": "The Four Seasons",
        "tag": "Year 1",
        "blurb": "Spring, summer, autumn and winter — how nature changes.",
        "pages": [
            {"emoji": "🔄", "heading": "Four seasons",
             "text": "A year has four seasons: spring, summer, autumn and winter. Then it all "
                     "starts again!"},
            {"emoji": "🌷", "heading": "Spring",
             "text": "In spring, buds open, flowers like daffodils appear and lambs are born. "
                     "The days get longer and warmer."},
            {"emoji": "☀️", "heading": "Summer",
             "text": "Summer is usually the warmest season. Days are long and trees are full of "
                     "green leaves. Wear sun cream and a hat!"},
            {"emoji": "🍂", "heading": "Autumn",
             "text": "In autumn, leaves on deciduous trees turn red, orange and brown and fall. "
                     "Conkers and acorns drop. Some animals get ready to hibernate."},
            {"emoji": "❄️", "heading": "Winter",
             "text": "Winter is usually the coldest season. There might be frost, ice or snow. "
                     "Many trees have bare branches.",
             "fact": "Hedgehogs hibernate — they sleep through the winter!"},
        ],
        "words": [
            ("season", "one of the four parts of the year"),
            ("spring", "the season when plants start to grow again"),
            ("summer", "the warmest season"),
            ("autumn", "the season when leaves fall"),
            ("winter", "the coldest season"),
            ("hibernate", "sleep through the winter"),
        ],
        "talk": "Which season is it now? What changes can you see outside?",
        "quiz": [
            {"q": "In which season do leaves fall from deciduous trees?",
             "options": ["Spring", "Autumn", "Summer"], "answer": 1,
             "why": "Leaves change colour and fall in autumn."},
            {"q": "Which season is usually the coldest?",
             "options": ["Winter", "Summer"], "answer": 0,
             "why": "Winter is usually the coldest season."},
            {"q": "When are lambs usually born?",
             "options": ["Spring", "Autumn"], "answer": 0,
             "why": "Spring is when lots of baby animals are born."},
            {"q": "How many seasons are there?",
             "options": ["Two", "Four", "Twelve"], "answer": 1,
             "why": "Spring, summer, autumn and winter."},
        ],
    },
    {
        "id": "weather-and-day-length",
        "area": "seasons",
        "emoji": "🌤️",
        "title": "Weather and Day Length",
        "tag": "Year 1",
        "blurb": "Sunny, rainy, windy, snowy — and why winter days are short.",
        "pages": [
            {"emoji": "🌦️", "heading": "Types of weather",
             "text": "Weather can be sunny, cloudy, rainy, windy, foggy, frosty or snowy. "
                     "It can change from day to day — even hour to hour!"},
            {"emoji": "🌡️", "heading": "Measuring weather",
             "text": "A thermometer measures how hot or cold it is. A rain gauge collects rain to "
                     "measure how much fell. A windsock shows which way the wind blows."},
            {"emoji": "🌅", "heading": "Long summer days",
             "text": "In summer, the sun rises early and sets late, so days are long and nights "
                     "are short. It can still be light at bedtime!"},
            {"emoji": "🌙", "heading": "Short winter days",
             "text": "In winter, the sun rises late and sets early. Days are short and it gets "
                     "dark before teatime.",
             "fact": "The longest day of the year is in June. The shortest is in December."},
            {"emoji": "📒", "heading": "Weather diary",
             "text": "Keep a weather chart for a week. Draw a symbol for each day's weather. "
                     "Which weather happened most?"},
            {"emoji": "😎", "heading": "Sun safety",
             "text": "Never look straight at the Sun, even with sunglasses. In summer, wear a "
                     "hat and sun cream."},
        ],
        "words": [
            ("weather", "what it is like outside — sunny, rainy, windy…"),
            ("thermometer", "measures how hot or cold it is"),
            ("forecast", "what the weather will probably be"),
            ("day length", "how long it is light for"),
        ],
        "talk": "What's the weather like today? What will you wear because of it?",
        "quiz": [
            {"q": "What measures temperature?",
             "options": ["A thermometer", "A rain gauge", "A ruler"], "answer": 0,
             "why": "A thermometer tells you how hot or cold it is."},
            {"q": "When are days longest?",
             "options": ["Summer", "Winter"], "answer": 0,
             "why": "In summer the sun rises early and sets late."},
            {"q": "Which month has the shortest day?",
             "options": ["June", "December"], "answer": 1,
             "why": "The shortest day is in December, in winter."},
            {"q": "What should you never do?",
             "options": ["Look straight at the Sun", "Wear a hat", "Keep a weather diary"],
             "answer": 0, "why": "Looking at the Sun can damage your eyes."},
        ],
    },
]
