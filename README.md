# MIG: Metadata Image Generator

Welcome to MIG. This simple script was made to solve the particular problem some NFT creators face when creating NFTs in a way that doesnt generate metadata.

NOTE: This example is assuming youre using factoria.app to create your NFT collection. It should work for other situations, but some tweaking might be necessary.


## How to run
1. Clone project.
2. Upload your files to IPFS via factoria. This will generate image JSON files for each file uploaded.
3. Download the created image files.
4. Extract downloaded ZIP and drop the files into the cloned project directory called newImagesJSON.
5. Take the IPFS image URI, extract the final 3 characters and the / before the file name like so (extract this 6im/ from this ..6im/1.json )
6. Replace the URI extract in line 53 of the code ( .split('6im/')[1] ) with your URI extract (replace 6im/ with your extract)
5. Run script with python3 mig.py
