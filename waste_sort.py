import streamlit as st

tab1,tab2,tab3=st.tabs(["Home","Scan & Sort","About me"])

with tab1:
    st.title("Waste : Scan & Sort")
    col1,col2=st.columns(2)
    with col1:
        st.header("Welcome to Waste: Scan&Sort, a smart waste segregation platform.")
        st.write("At Waste: Scan&Sort, we aim to revolutionize the way we manage waste by leveraging cutting-edge technology. Our platform uses advanced machine learning algorithms to identify and classify waste into two major categories: Biodegradable and Non-Biodegradable. It is very important to segregate waste into these two categories for efficient waste management and environmental protection. Biodegradable waste, such as food scraps and garden waste, decomposes naturally and can be composted to create nutrient-rich soil, reducing landfill waste and supporting sustainable agriculture. Non-biodegradable waste, like plastics and metals, does not break down easily and can persist in the environment for decades, causing pollution and harming ecosystems. Proper segregation enables recycling, reducing the need for raw materials and energy-intensive production processes. It also prevents contamination of recyclable materials, ensuring their effective reuse.Additionally, separating waste minimizes greenhouse gas emissions from landfills, as biodegradable waste in mixed landfills produces methane, a potent greenhouse gas. By segregating waste, we contribute to cleaner surroundings, conserve resources, and support a circular economy, fostering a healthier planet for future generations.")
        st.write("How does this program work? Simply upload an image of your waste on the Scan & Sort page, and Waste: Scan&Sort will analyze it, helping you make more informed decisions about waste disposal. You will get immediate results with tips on how to dispose of or recycle the waste properly.Why is this important? Proper waste segregation is crucial for reducing landfill waste, conserving natural resources, and protecting our environment.Once your waste is segregated non-biodegradable waste can be used eco-friendly through recycling, upcycling, and repurposing. Plastics, metals, and glass can be recycled into new products, reducing the need for raw materials and energy consumption. Upcycling transforms waste into useful or decorative items, like turning old containers into planters or crafting art from discarded materials. Repurposing involves finding new uses for items, such as using jars for storage or tires as garden decorations. Proper disposal at recycling centers ensures these materials are processed responsibly. Adopting these practices not only reduces environmental pollution but also conserves resources, promoting a sustainable and eco-friendly lifestyle. On the other hand , biodegradable waste can be used for composting, which turns organic materials like food scraps, leaves, and garden waste into nutrient-rich compost for gardening and agriculture. This process reduces landfill waste and minimizes greenhouse gas emissions. Biodegradable waste can also be used for vermicomposting, where earthworms break it down into high-quality fertilizer. Additionally, it can serve as feedstock for biogas plants, producing renewable energy and organic slurry as a byproduct. Using biodegradable waste in these ways not only reduces environmental pollution but also enhances soil fertility, conserves natural resources, and supports a sustainable cycle of waste-to-resource conversion.Let Waste: Scan&Sort guide you in making smarter waste disposal choices, reducing your environmental footprint, and contributing to a more eco-conscious world. Together , we can build a cleaner future ! Start sorting your waste now with Waste: Scan & Sort !")
    with col2:
        st.image("https://rekart.co.in/uploads/blog/navigating-the-_waste-landscape.jpg", width=900)
with tab2:
    st.title("Scan & Sort")
    col1,col2,col3=st.columns(3)
    with col1:
        st.header("Scan")
        file= st.file_uploader("Upload an image of your waste here")
        st.button("Submit")

                
    with col2:
        st.header("Sort")
        #st.image("https://cdn-icons-png.flaticon.com/512/10004/10004491.png", width=200)
        #st.header("Sort")
    with col3:
        st.image("https://cdn-icons-png.flaticon.com/512/10004/10004491.png", width=200)

with tab3:
    col1,col2=st.columns(2)
    with col1:
        st.title("About me")
        st.write("Hello ! I am Diza Uppal , a student studying in Sanskriti School, New Delhi. I started this project to increase awareness about proper waste segregation and environmental conservation.  I was shocked by the number of deaths of marine animals in a nearby river caused due to the ingestion and entanglement of non biodegradable wastes  . The unsegregated wastes in landfills release toxins into these water sources, harming aquatic ecosystems. The non-biodegradable waste, such as plastics and metals, were leaching harmful chemicals into the soil, affecting its fertility. On the other hand biodegradable wastes decompose in landfills without proper treatment , releasing methane , a potent greenhouse gas causing global warming .By seeing all these harmful consequences, I realized the need to segregate waste products properly . Proper segregation enables recycling, reducing the need for raw materials and energy-intensive production processes. It also prevents contamination of recyclable materials, ensuring their effective reuse. Additionally, separating waste minimizes greenhouse gas emissions from landfills, as biodegradable waste in mixed landfills produces methane, a potent greenhouse gas. By segregating waste, we contribute to cleaner surroundings, conserve resources, and support a circular economy, fostering a healthier planet for future generations. My goals with this project are to raise the awareness for waste segregation in general and to gain popularity for my scanning to provide a free first step to  conserve our environment through proper waste segregation!")
    with col2:
        st.title("Contact us")
        st.header("Contact us here !")
        st.write("Email : waste_sort.gmail.com")
        st.button("Youtube")
        st.button("Facebook")
        st.button("Instagram")

    


 



