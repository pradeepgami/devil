![image](https://github.com/user-attachments/assets/bb1e3d60-852f-4dcd-b21f-290eaf06ff6d)

---

# Music Streaming Smart Contract

## Vision

The Music Streaming project aims to provide a decentralized platform where artists can register their music tracks and receive royalties whenever users stream their songs. By using blockchain technology, this project offers a transparent way for artists to monetize their music while allowing listeners to directly support their favorite artists without intermediaries.

## Features

- **Register Music Track**: Artists can register their music tracks on the blockchain, providing a title and setting a price for streaming.
- **Stream Music Track**: Users can stream a music track by interacting with the smart contract, ensuring that royalties are directly paid to the artists.
- **Transparent Royalty System**: The platform ensures that payments are transparent, and artists receive fair compensation for each stream.

## Contract Address

- **Network**: Aptos Mainnet/Testnet
- **Contract Address**: `0xbc17e036a66ebb61aebffe16151923d3f25dfb2254963dc2a72643ae708f099d`

## How It Works

1. **Register Track**:

   - Artists call the `register_track` function to register a new music track.
   - The function takes the title of the track and the price for streaming as parameters, storing this information, including the artist's address, on the blockchain.

2. **Stream Track**:
   - Users can call the `stream_track` function to stream a music track registered by an artist.
   - Payment for streaming is assumed to be handled through other off-chain or on-chain mechanisms in future iterations.

## Future Scope

- **On-Chain Payment Handling**: Implement on-chain payment integration to allow users to pay the streaming fee directly using tokens, ensuring artists receive royalties for each stream.
- **Playlist Creation**: Add functionality for users to create and manage playlists of their favorite tracks.
- **Subscription Model**: Introduce a subscription feature where users can pay a recurring fee for unlimited streaming of tracks.
- **NFT Integration**: Allow artists to mint their tracks as NFTs, providing exclusive ownership options and additional revenue streams.
- **Analytics Dashboard**: Provide an analytics dashboard for artists to see metrics like the number of streams, earnings, and fan engagement.
- **Social Sharing and Fan Rewards**: Enable social sharing features to promote tracks and introduce a reward system for fans who actively engage and promote artists.

## Getting Started

- Clone this repository and install the necessary dependencies for the Aptos blockchain.
- Deploy the contract using your preferred deployment tool.
- Once deployed, artists can register their tracks, and users can stream the music through the smart contract functions.

## Contributing

We welcome contributions! If you have suggestions for improving the Music Streaming platform or want to add new features, feel free to open an issue or submit a pull request.

---

Feel free to modify and expand the README as your project evolves and new features are added!
