Title: Holiday Update, July 4, 2019
Date: 2019-07-04
Category: misc
Tags: bee-keeping, scuttlebutt, mesh, gypsy wagon


Happy Independence Day, my fellow Americans, and similar sentiments to my
international friends.

## Bee Journal

Our last hive inspection was early last month, and we decided to let some weeks
go by before we opened the hive again. We added a second brood super to the hive
during the last week of May, and upon our last inspection the colony had only
just started to draw comb on the new frames. It has been a long, cold spring
with lots of rain. The beehive, the garden have both developed slowly this year
for it.

It's been warmer this past couple of weeks, and both the gardens and the hive
have certainly perked up. Yesterday the colony started to beard on the front of
the apiary. I'd read that this was normal and could mean a healthy hive that
needed more room. We decided that bright and early this morning we would open
the hive, give a quick inspection and add a honey super. We'd been continuing to
feed until this point, and when I opened the top feeding super it was very full
of bees, the sugar jars covered and a thick cluster clung to the inside of the
cover when I lifted it. After giving a couple puffs of smoke to the entrance and
inside, I tapped off the bees and we lifted off the top brood super to see what
was going on below.

Confirming what we'd expected, the bottom brood super was full, all ten frames.
While we opted not to pull out any frames this time, it was easy to see bulging
drone caps and smooth worker caps from above. While we didn't see the queen, her
work is evident. When we open the hives we like to work fast, so we quickly
reassembled the hive, added the new honey super and closed it up. There were
still probably a couple of hundred bees clinging to the removed inner cover and
feeding super, so I tapped them off on top of the hive and put the equipment
away. Over the next hour the lingering bees found their way back inside, I hope
to start filling the honey super.

Speaking of honey, there were plenty of swollen honey cells at the top of the
brood frames, and a bit of comb had stuck to the bottom side of the inner cover.
We scraped this off and squeezed out our first taste of our backyard honey, and
it was good! I'm hopeful we will see our first harvest in August.

## Scuttlebutt, Decentralized Content

A couple of years ago I learned about and started using an interesting protocol
and application called [Scuttlebutt](https://scuttlebutt.nz). This is a
decentralized, peer to peer social network, more or less, built upon it's own
custom protocol and developed by some notable hackers in New Zealand. While I've
been using Scuttlebutt for some time, I'd fallen off since I don't really have
any friends on there, and I'd become disillusioned with some of the attitudes
expressed on the platform. A [recent
podcast](https://soundcloud.com/epicenterbitcoin/eb-290) featured Scuttlebutt's
(SSB) creator, Dominic Tarr, and after listening to it I've found my interest
renewed.

After having fired up my client, [Patchwork](https://github.com/ssbc/patchwork),
I waited for a few hundred content updates to sync and found the community to
which I'd connected to be about the same. The focus is certainly on the
development of the platform and the social concerns of that community, which
seems to be quite influenced by the thinkers at
[Loomio](https://www.loomio.org/) whom I admire. Much talk of consensus and
inclusion. I've begun once again to post here and there, in Esperanto and
concerning bees, so far.

I've also decided to try hosting my own pub server, a sort of super-peer used to
get around the limitations of IP4 and NAT, and to pull my community focus
towards something more local to myself. I've nearly got a working kubernetes
deployment assembled, just working through some peculiarities around loading
configuration into a hosted volume. More to come there, as I expect I'll have it
working by the end of the long holiday weekend.

## Mesh Networking, Redux

I'm starting to revive an older project. A couple of Pi-days ago I gathered all
the [RaspberryPi](https://www.raspberrypi.org/) single-board computers I could
borrow and built a small mesh network using the Open Mesh Project's
[batman-adv](https://www.open-mesh.org/projects/batman-adv/wiki). I had a bunch
of success, and I even teamed up with a colleague to run his Kubernetes cluster
on it. I started writing some code using the
[alfred](https://www.open-mesh.org/projects/alfred/wiki) distributed data store,
and there is a [GitHub project](https://github.com/coyote240/alfred-client) with
setup instructions and some of the Python I wrote to handle native messages.
Like a lot of projects, after the initial push my effort petered out, but this
is tech I care about and I finally am starting to push myself to pick it up
again.

During my [recent Erlang training]({filename}/erlang-training.md), I
realized that the binary message passing that I'd been using Python for might be
better handled using Erlang's excellent binary pattern matching. It should be
fairly straight-forward to handle any combination of Alfred or batman-adv
messages quickly. I've got a handful of Pi Zero Ws ready for the task, I'm
starting to get the basics set up and to experiment running Erlang on each.

## Even Tinier House?

So, last thing, we traveled to visit the in-laws and our oldest son last
weekend. We met his girlfriend for the first time. She's a bit of a bad-ass, I
have to admit, and she lives in a ~200sqft. tiny house she built with her
family. We drove out to take a look and I was immediately inspired. No, tiny
house living is not in my future, but I have daydreamed in the past about
building a Gypsy or Basque style wagon into the back of a 1967 Ford F250 we have
parked out back. I'm starting to see what it would take to get the truck moving
again (tires, fresh gas, etc.) and maybe start to sketch out some plans.

Serendipitously, my mother sent me this great book for my birthday just a few
days after we got back. Derek "Deek" Diedricksen at
[RelaxShacks](https://relaxshacks.blogspot.com/) wrote this great book, __Humble
Homes, Simple Shacks, Cozy Cottages, Ramshackle Retreats, Funky Forts and
Whatever Else We Could Squeeze in Here!__. His web site is a bit of a nightmare,
but look him up on that video streaming site I heard of or check out the book.
It's a lot of fun and is full of inspiring ideas that just might help lead to a
hand crafted camper truck.

Ĝis la revido, kaj feliĉa kodumado!
