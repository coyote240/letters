Title: Weekend Update, May 12, 2019
Date: 2019-05-12
Category: misc
Tags: beekeeping, gardening, devops


## Bee Journal

Saturday we opened the bee hive for the second time since they were introduced
two weeks ago. The first inspection was expected at one week, which we did, but
we didn't see eggs as we'd hoped, so we opted to try again this week. The queen
did not disappoint! Comb has been drawn out from the fourth to the eighth frame.
According to my notes, this is to be expected. Within that comb we have many
plump, white larvae, loads of capped cells along with plenty of brood honey. We
weren't able to locate the queen, a skill we sorely need to develop, so we'll
have to be content with the signs we've seen.

It's been rainy, snowy and cold all week, so activity outside the hive has been
way down. The last two days has been warm and sunny so the bees have been out in
force. During the warm part of the day you can see bees constantly
criss-crossing the airspace above our yard. Watching the entrance you can see
them returning laden with pollen in colors from white and yellow, through rich
oranges and even the occasional red. It is beautiful to watch.

I don't expect to open the hive again for at least two more weeks, during which
time we hope to see 70-80% of the frames full in this first super, and perhaps
we'll try again to find the queen. These goals met, we can add a second deep
super full of frames to extend the brood.

I'd love to put up pictures of what I'm describing, but until I can automate
stripping EXIF from my photographs, well, you know. More to come here.

## Garden Planted

Well, we put seeds in the ground anyway. Being Mother's Day, the Mrs. wanted
simply to hang around the yard, clean it up a bit for guests who will be
visiting in the next week, and put more effort into the gardens. We'd already
added a small amount of sulphur on all three gardens after the Mrs. found we
were a bit low.  After some debate and further reading we decided to add manure
again this year.  There had been some doubt: last year's yield left much to be
desired, and we'd been speculating all winter what had gone wrong. My theory was
that our soil's nutrients had been depleted. We agreed that we hadn't been
watering enough, and research supports this assumption. Manure and/or compost
seem to be important for soil building every year, so we made the trip out for 7
bags between the three gardens.

My best friend lives a few blocks away and he owns a small tiller that we borrow
when needed. He'd complained that it wasn't running well. I started it up to see
thick blue smoke and yes, it was running poorly. I drained some of the oil, he'd
over filled it, and replaced the gas. Ran fine for me and we tilled the manure
into the gardens in short order. Being such a nice day we went ahead and put
seeds into the ground: the usual pumpkins, squash and cucumbers in one garden
and kale, carrots, cilantro and dill in the garden nearest the bee hive. There
is one garden yet to be planted, but this will be live plants from the nursury,
tomatoes and chilis. That we won't do for a couple more weeks.

## API Gateway/Proxy Evaluation

This past week at work I've continued to evaluate API gateway and proxy options.
We already have [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/)
in place, which our SREs are already quite fond of, but we've extended our
exploration to [Kong](https://konghq.com) and [Ambassador](https://www.getambassador.io)
as well. There are things I like about all of them, but I'm interested in
building upon what we have if we can. We have specific authentication needs for
a couple of our applications for which it doesn't seem to matter which proxy we
choose, some custom code will have to be written. Look for an article here soon
that will go into some of the problems I have to solve, and how I'm using some
powerful features of the NGINX Ingress Controller to reframe the conversation.

## Current Media Consumption

I read a fair amount of science fiction and I'm particularly a fan of pulp
novels from the 50's through the 70's. This week I'm reading [Rendezvous with
Rama](https://www.goodreads.com/book/show/112537.Rendezvous_with_Rama) by Arthur
C. Clarke. This is the six novel by Clarke I've read, and I appreciate his brand
of "hard" science fiction.

We watched and enjoyed [Hanna](https://www.imdb.com/title/tt6932244/), though I
understand the ratings weren't that good. Two lead actors came from The Killing,
the first season I liked. The lead actress was great and it had a decent
soundtrack that I might be able to code to.

[Cory Doctorow's](https://craphound.com) new book was great as always, though I
don't care to write a review here. As he does to support his books he's been
doing the interview circuit. Many of his interviews end up on his
[podcast](https://craphound.com/category/podcast/). The themes tend to repeat
but bear repeating, give them a listen.

That's enough or too much for now. More later.
