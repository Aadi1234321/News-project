from app import db, News, app

def seed_data():
    with app.app_context():
        # Clear existing
        db.drop_all()
        db.create_all()

        news1 = News(
            title="Quantum Leap: Nexus Computing Solves the Unsolvable",
            content="Today, Nexus Labs announced a breakthrough in quantum computing that promises to revolutionize cryptography and material science. The new processor, codenamed 'Aether', operates at room temperature and maintains coherence for record-breaking durations.\n\nResearchers believe this will lead to advancements in medicine, battery technology, and artificial intelligence that were previously thought to be decades away. The global scientific community is buzzing with excitement as the first public demonstrations are scheduled for next month.",
            author="Dr. Sarah Chen",
            category="Technology",
            image_url="/static/images/tech.png",
            area="Global"
        )

        news2 = News(
            title="Green Oasis: New Eco-Park Opens in Downtown",
            content="The long-awaited 'Sky Garden' has finally opened its doors to the public. Spanning three city blocks and elevated 50 feet above the ground, this architectural marvel incorporates sustainable water recycling and solar-powered lighting.\n\nLocal residents have praised the design, noting its contribution to urban biodiversity and providing a much-needed breath of fresh air in the heart of the bustling metropolis. The park also features interactive glass walkways that display information about the local flora and fauna.",
            author="James Rivera",
            category="Local",
            image_url="/static/images/park.png",
            area="Downtown"
        )

        news3 = News(
            title="Neo-Circuit: The Future of Racing is Here",
            content="The inaugural Neo-Circuit Grand Prix took place last night under the neon lights of Tokyo. Featuring electric vehicles capable of reaching speeds over 400km/h, the event drew a record-breaking crowd both in person and in the metaverse.\n\nVictory went to rookie driver Akira Sato, who mastered the complex mag-lev tracks with unprecedented precision. Fans are already calling it the greatest sporting event of the century, highlighting the perfect blend of human skill and high-tech engineering.",
            author="Marco Veloce",
            category="Sports",
            image_url="/static/images/sports.png",
            area="East City"
        )

        db.session.add_all([news1, news2, news3])
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
