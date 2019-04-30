Meeting Minute - Roadmap 2019-04-29
===
###### tags: `Meeting`
-------------------------------------------------------------

:::info
- **Location:** B53/4025
- **Date:** 2019-04-29
- **Agenda**
1. Intro from DT
2. Dev team proposal (from SR core team)
3. Meta - Process for managing processes?
4. Current development work
- **Participants:**
    - Dan Trickey (DT)
    - Dan Hobson (DH)
    - Alex Lockwood (AL)
    - Kajatan Champlewski (KC)
    - Joe Morton (JM)
    - Kier Davis (KD)
    - Andy Barrett-Sprot (ABS), remote
    - Tom Wheal (TW)
    - Rob Gilton (RG)
    - Josh Holland (JHol), remote
    - Jake Howard (JHow), remote
    - Richard Barlow (RB), remote
    - James Seden Smith (JSS)
    - Antione Petty (AP)
    - Tyler Ward (TW)
    - Peter Law (PL)
- **Chair:** DT <dgt1g17@soton.ac.uk>
- **Minutes:** DH <dsh1g18@soton.ac.uk>
- **Minutes Archive:** - [Available here](https://github.com/s-r-o/minutes/)

:::


-------------------------------------------------------------

# Agenda
1. Intro from DT
    - clarification of "SourceBots", "Hills Road", "Robocon"
    - Plans for next 6 months
    - Deadlines:
        - Smallpiece 2019 (August)
        - SR Kickstart 2019-20
    - Introductions of people present
2. Dev team proposal (from SR core team)
    - link [here](https://github.com/srobo/dev-team-proposal)
    - Need dedicated dev strategy
    - RG
        - Dev cover kit should only at first (long term development), then expand
        - "kit team"?
        - responsible for serving kit to core team
        - cover hardware, software, tools (IDE)
        - 3-5 people responsible, selected by trustees ~ every ~2 years
            - set long term direction
            - handle communications with teachers, students etc
        - "competition software" could follow same model for software specific to each competition e.g. screens
    - TW
        - separation of teams requires good planning so tasks aren't orphaned
        - asset tracking should stay with kit
    - RB
        - Agree get started with Kit Team, then model other teams to follow
    - ABS
        - Need to kepp scope managable as to avoid "make everything better" trap
    - Important for moving towards sustainability of SR
    - Proposal to be formalised and made available for review
        - propose a 2nd call after written
    - DT, TW
3. Meta - Process for managing processes?
    - I.e. formalise the process for making proposals to trustees
        - E.g. Agree on version numbering system
        - System for communications ascociated with changes
    - DT, TW to do with kit team proposal
4. Current development work
    - Write up results of interviews from teams
    - Brain board (ODroid)
        - No longer manufactured -> replace
            - Will need to decide on replacement
                - SourceBots and Robocon using RPi3
        - Intended to be replaced, hence the design separation of power and brain boards
            - keep flexibility (avoid device-specific dev like RPi hats)
            - power concerns: need to check power board can supply new brain boards
            - RPis lack protection on GPIO
        - Transition could be staggered if we are willing to ship a mix of boards
    - SR boards firmware
        - Is old, with improvements and 'quirks' to go through
        - TW has a chance to be paid for charity dev work
        - Automated testing would help us a lot
            - Build a basic test system for software and for hardware
        - Python2 will deprecated soon -> Python3
            - Upgrade existing API?
            - Or j5: platform agnositic API system with similar competitor-facing API
                - Working currently, should meet Smallpiece deadline
                - Hoping that competitors will look through it
                - Nice to be able to support kit for all competitions (Smallpiece, SR, Robocon)
        - Need to decide what to deploy for smallpiece 2019
            - JM as SourceBots director to have executive decision
        - OS choice
            - boot time is slow
            - read-only filesystem would protect against power loss
            - Alpine OS?
        - IDE
            - Online IDE is highly requested from competitiors
            - Existing IDE should handle python3
        - Comp screens
            - Migrate?


-------------------------------------------------------------

## ACTION POINTS
- [ ] [name=DT, TW] : Kit team proposal to be formalised and made available for review
- [ ] [name=DT, TW] : consider proposal procedure whilst doing kit team proposal
- [ ] [name=JM] : To have final decision on choice of kit for Smallpiece 2019

## Notes 
<!-- Other important details discussed during the meeting can be entered here. -->
